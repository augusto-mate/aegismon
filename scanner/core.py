# aegismon/scanner/core.py - VERSÃO FINAL CORRIGIDA COM FILTRO

import os
import hashlib
from datetime import datetime
from ..logging.logger import get_logger
from .signatures import SIGNATURE_DB

logger = get_logger(__name__)

# --- Lógica de Severidade ---
# Nota: Esta lógica deve corresponder a tests/test_scanner.py
def calculate_severity(signatures, heuristics):
    """ Calcula o nível de severidade (none, low, medium, high). """
    if signatures:
        return "high"
    
    heuristic_score = sum(h.get('score', 0) for h in heuristics)
    
    if heuristic_score >= 70:
        return "medium"
    if heuristic_score > 0:
        return "low"
    
    return "none"

# --- Classe ScanResult ---
class ScanResult:
    def __init__(self, file, signatures=None, heuristics=None, hashes=None):
        # CORREÇÃO ANTERIOR: O argumento é 'file'
        self.file = file 
        self.signatures = signatures if signatures is not None else []
        self.heuristics = heuristics if heuristics is not None else []
        self.hashes = hashes if hashes is not None else {}
        self.severity = calculate_severity(self.signatures, self.heuristics)

    def as_dict(self):
        """ Retorna o resultado como um dicionário. """
        return {
            "file": self.file,
            "signatures": self.signatures,
            "heuristics": self.heuristics,
            "hashes": self.hashes,
            "severity": self.severity,
        }

# --- Classe Scanner ---
class Scanner:
    
    def __init__(self, hash_algs=['md5', 'sha256']):
        self.hash_algs = hash_algs
        self.total_scanned = 0

    def _compute_hashes(self, file_path):
        """ Calcula hashes para os algoritmos definidos. """
        hashes = {alg: hashlib.new(alg) for alg in self.hash_algs}
        
        try:
            with open(file_path, 'rb') as f:
                while chunk := f.read(4096):
                    for h in hashes.values():
                        h.update(chunk)
            return {alg: h.hexdigest() for alg, h in hashes.items()}
        except Exception as e:
            logger.error(f"Erro ao calcular hash de {file_path}: {e}")
            return {}

    def _match_signatures(self, file_hashes):
        """ Verifica se algum hash corresponde ao banco de dados de assinaturas. """
        detected_signatures = []
        for threat_name, threat_data in SIGNATURE_DB.items():
            for alg, hash_value in file_hashes.items():
                if threat_data.get(alg) == hash_value:
                    detected_signatures.append(threat_name)
                    break 
        return detected_signatures

    def _run_heuristics(self, file_path):
        """ Aplica regras heurísticas simples (exemplo). """
        heuristics = []
        file_size = os.path.getsize(file_path)
        
        # Heurística 1: Arquivos muito grandes
        if file_size > (10 * 1024 * 1024): # > 10MB
            heuristics.append({"rule": "large_file_size", "score": 40})
        
        # Heurística 2: Arquivos sem extensão
        if '.' not in os.path.basename(file_path):
            heuristics.append({"rule": "no_file_extension", "score": 75})
            
        return heuristics

    def _scan_file(self, file_path):
        """ Realiza o scan completo em um único arquivo. """
        self.total_scanned += 1
        
        file_hashes = self._compute_hashes(file_path)
        signatures = self._match_signatures(file_hashes)
        heuristics = self._run_heuristics(file_path)

        return ScanResult(
            file=file_path,
            signatures=signatures,
            heuristics=heuristics,
            hashes=file_hashes
        )

    def scan_path(self, path):
        """ Inicia a varredura (arquivo ou diretório). """
        all_results = []
        start_time = time.time()
        self.total_scanned = 0

        # ... (lógica de iteração de diretório/arquivos, simplificada para focar no retorno) ...
        
        if os.path.isfile(path):
            all_results.append(self._scan_file(path))
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    all_results.append(self._scan_file(file_path))
        else:
            logger.error(f"Caminho não encontrado ou inválido: {path}")
            return {}

        end_time = time.time()

        # >>>>>> FILTRO DE CORREÇÃO FINAL <<<<<<
        # 1. Filtra resultados para incluir APENAS DETECÇÕES (severity != 'none')
        filtered_results = [r for r in all_results if r.severity != 'none']
        
        # 2. Converte os resultados filtrados para dicionários
        results_list = [r.as_dict() for r in filtered_results]

        return {
            "target": path,
            "scan_date": datetime.now().isoformat(),
            "results": results_list,
            "stats": {
                "duration": f"{end_time - start_time:.2f}s",
                "scanned": self.total_scanned,
                "detections": len(filtered_results),
            }
        }
