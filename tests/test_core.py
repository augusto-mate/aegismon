# tests/test_core.py
import pytest
from aegismon.scanner.core import ScanResult, Scanner

def test_scanresult_basic_properties():
    # Cria um resultado de teste
    result = ScanResult(
        file_path="dummy.txt",
        signature="EICAR_TEST_FILE",
        severity="low",
        description="Arquivo de teste EICAR"
    )

    # Valida atributos
    assert result.file_path == "dummy.txt"
    assert result.signature == "EICAR_TEST_FILE"
    assert result.severity == "low"
    assert "EICAR" in result.description

def test_scanner_detects_signature(tmp_path):
    # Cria arquivo temporário com conteúdo que simula assinatura
    test_file = tmp_path / "eicar.txt"
    test_file.write_text("X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*", encoding="utf-8")

    scanner = Scanner()
    results = scanner.scan_file(str(test_file))

    # Deve detectar pelo menos uma assinatura
    assert isinstance(results, list)
    assert any(r.signature == "EICAR_TEST_FILE" for r in results)

def test_scanner_no_detection(tmp_path):
    # Cria arquivo temporário sem assinatura conhecida
    test_file = tmp_path / "clean.txt"
    test_file.write_text("conteúdo limpo sem malware", encoding="utf-8")

    scanner = Scanner()
    results = scanner.scan_file(str(test_file))

    # Não deve detectar nada
    assert results == []
