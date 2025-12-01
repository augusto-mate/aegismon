# aegismon/scanner/core.py
import hashlib
import os
import time
from .signatures import SIGNATURE_DB # Assinaturas em vez de KNOWN_SIGNATURES

# ScanResult para tipagem e cálculo de severidade
class ScanResult:
    def __init__(self, file, signatures=None, heuristics=None, hashes=None):
        self.file = file
        self.signatures = signatures or []
        self.heuristics = heuristics or []
        self.hashes = hashes or {}

    @property
    def severity(self):
        """Define severidade com base em assinaturas e heurísticas."""
        if self.signatures:
            return "high"
        # Média ou pontuação máxima para MEDIUM/LOW
        if any(h["score"] >= 70 for h in self.heuristics):
            return "medium"
        if self.heuristics:
            return "low"
        return "none"

    def as_dict(self):
        return {
            "file": self.file,
            "signatures": self.signatures,
            "heuristics": self.heuristics,
            "hashes": self.hashes,
            "severity": self.severity
        }

class Scanner:
    """Scanner com assinaturas, hashing e heurísticas."""
    def __init__(self, algorithms=("md5", "sha1", "sha256")):
        self.algorithms = algorithms

    def _compute_hashes(self, file_path):
        """Calcula hashes configurados."""
        h = {alg: hashlib.new(alg) for alg in self.algorithms}
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    for alg in h.values():
                        alg.update(chunk)
        except Exception:
            return {}
        return {k: v.hexdigest() for k, v in h.items()}

    def _match_signatures(self, hashes):
        """Compara hashes com o banco de assinaturas carregado."""
        found = []
        for signature, known_hashes in SIGNATURE_DB.items():
            if any(h in known_hashes for h in hashes.values()):
                found.append(signature)
        return found
    
    def _run_heuristics(self, file_path):
        """Executa heurísticas e atribui pontuação de risco."""
        heuristics = []
        try:
            size = os.path.getsize(file_path)
            _, ext = os.path.splitext(file_path)
            basename = os.path.basename(file_path)
        except Exception:
            return []

        # Heurística 1: Arquivo muito grande (> 50MB)
        if size > 50 * 1024 * 1024:
            heuristics.append({
                "rule": "large_file",
                "score": 40,
                "description": "Arquivo muito grande para uso comum."
            })
        
        # Heurística 2: Extensão suspeita
        suspicious_ext = {".dll", ".sys", ".scr", ".pif", ".tmp", ".exe"}
        if ext.lower() in suspicious_ext:
            heuristics.append({
                "rule": "suspicious_extension",
                "score": 60,
                "description": f"Extensão suspeita detectada: {ext}"
            })
        
        # Heurística 3: Nome disfarçado (ex: .txt.exe)
        # Verifica se há mais de um ponto (além da extensão final) e se é executável
        if ext.lower() in {".exe", ".scr"} and basename[:-len(ext)].count('.') > 0:
            heuristics.append({
                "rule": "double_extension",
                "score": 80,
                "description": "Arquivo com dupla extensão potencialmente maliciosa."
            })
        
        return heuristics

    def scan_file(self, file_path):
        hashes = self._compute_hashes(file_path)
        signatures = self._match_signatures(hashes)
        heuristics = self._run_heuristics(file_path)

        return ScanResult(
            file=file_path, 
            signatures=signatures, 
            heuristics=heuristics, 
            hashes=hashes
        )
    
    def scan_path(self, path):
        start = time.time()
        all_results = []
        scanned_count = 0
        error_count = 0

        if os.path.isfile(path):
            try:
                all_results.append(self.scan_file(path))
                scanned_count = 1
            except Exception:
                error_count = 1
        else:
            for root, _, files in os.walk(path):
                for f in files:
                    full_path = os.path.join(root, f)
                    scanned_count += 1
                    try:
                        all_results.append(self.scan_file(full_path))
                    except Exception:
                        error_count += 1
                        
        duration_ms = int((time.time() - start) * 1000)

        return {
            "target": path,
            "results": [r.as_dict() for r in all_results],
            "stats": {
                "scanned": scanned_count,
                "duration_ms": duration_ms,
                "errors": error_count
            }
        }
