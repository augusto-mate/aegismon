# tests/test_scanner.py
from aegismon.scanner.core import ScanResult

# Teste 1: Severidade (Nenhuma)
def test_scan_result_severity_none():
    """ Testa a severidade quando não há detecções. """
    result = ScanResult(file="/caminho/limpo.txt")
    assert result.severity == "none"

# Teste 2: Severidade (Alta - Assinaturas)
def test_scan_result_severity_high_signatures():
    """ Testa a severidade quando há assinaturas detectadas. """
    # Assinaturas geram severidade ALTA
    result = ScanResult(
        file="/caminho/malware.exe",
        signatures=["EICAR_Test_File"]
    )
    assert result.severity == "high"

# Teste 3: Severidade (Média - Heurísticas Altas)
def test_scan_result_severity_medium_heuristics():
    """ Testa a severidade quando há heurísticas de pontuação alta (>= 70). """
    # Heurísticas de pontuação 70+ geram severidade MÉDIA
    result = ScanResult(
        file="/caminho/suspeito.dll",
        heuristics=[{"rule": "suspicious_ext", "score": 75}] 
    )
    assert result.severity == "medium"

# Teste 4: Severidade (Baixa - Heurísticas Baixas)
def test_scan_result_severity_low_heuristics():
    """ Testa a severidade quando há heurísticas de pontuação baixa (< 70). """
    # Heurísticas de pontuação < 70 geram severidade BAIXA
    result = ScanResult(
        file="/caminho/arquivo.tmp",
        heuristics=[{"rule": "large_file", "score": 40}] 
    )
    assert result.severity == "low"