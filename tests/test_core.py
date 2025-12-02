# tests/test_core.py - VERSÃO CORRIGIDA
import os
import time
from unittest.mock import patch, MagicMock
from aegismon.scanner.core import Scanner, ScanResult

# Define um caminho de arquivo mock para teste
MOCK_FILE = "/tmp/test_file.txt"

# --- Testes de ScanResult (Propriedades Básicas) ---

def test_scanresult_basic_properties():
    """ Testa a inicialização e o output do ScanResult. """
    # CORREÇÃO 1: Usa 'file=' em vez de 'file_path='
    result = ScanResult(
        file=MOCK_FILE,
        hashes={"md5": "abc", "sha256": "def"},
        signatures=["signature_x"],
        heuristics=[{"rule": "r1", "score": 80}]
    )
    assert result.file == MOCK_FILE
    # Assinatura garante severidade 'high'
    assert result.severity == "high" 

    result_dict = result.as_dict()
    assert result_dict["file"] == MOCK_FILE
    assert "hashes" in result_dict
    assert "severity" in result_dict

# --- Testes do Scanner (API de Saída) ---

# Mock para simular um arquivo com assinatura maliciosa
@patch('os.path.isfile', return_value=True)
@patch('aegismon.scanner.core.Scanner._compute_hashes', return_value={"md5": "eicar_hash"})
@patch('aegismon.scanner.core.Scanner._match_signatures', return_value=["EICAR_Test_File"])
@patch('aegismon.scanner.core.Scanner._run_heuristics', return_value=[])
def test_scanner_detects_signature(mock_heur, mock_sig, mock_hash, mock_isfile):
    """ Testa se o scanner retorna a estrutura de dicionário correta com uma detecção. """
    scanner = Scanner()
    
    # scan_path é chamado com um caminho (mockamos que é um arquivo)
    results_output = scanner.scan_path(MOCK_FILE) 

    # CORREÇÃO 2: Espera a estrutura de dicionário da v4 (com 'results' e 'stats')
    assert isinstance(results_output, dict)
    assert "stats" in results_output
    assert "results" in results_output
    
    # Verifica a detecção DENTRO da lista 'results'
    assert len(results_output["results"]) == 1
    assert results_output["results"][0]["signatures"] == ["EICAR_Test_File"]
    assert results_output["results"][0]["severity"] == "high"

# Mock para simular um arquivo limpo
@patch('os.path.isfile', return_value=True)
@patch('aegismon.scanner.core.Scanner._compute_hashes', return_value={"md5": "clean_hash"})
@patch('aegismon.scanner.core.Scanner._match_signatures', return_value=[])
@patch('aegismon.scanner.core.Scanner._run_heuristics', return_value=[])
def test_scanner_no_detection(mock_heur, mock_sig, mock_hash, mock_isfile):
    """ Testa se o scanner retorna a estrutura de dicionário correta sem detecções. """
    scanner = Scanner()
    results_output = scanner.scan_path(MOCK_FILE)

    # CORREÇÃO 3: Verifica se a lista 'results' está vazia
    assert isinstance(results_output, dict)
    assert "results" in results_output
    assert results_output["results"] == []
    assert results_output["stats"]["scanned"] == 1
