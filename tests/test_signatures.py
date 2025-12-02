# tests/test_signatures.py
import json
import tempfile
import os
import pytest

from aegismon.scanner.signatures import SIGNATURE_DB, get_signature, load_signature_file

def test_signature_db_contains_eicar():
    # Verifica se a assinatura EICAR está presente
    sig = get_signature("EICAR_TEST_FILE")
    assert sig is not None
    assert sig["severity"] == "low"

def test_get_signature_not_found(caplog):
    # Verifica comportamento quando assinatura não existe
    sig = get_signature("UNKNOWN_SIGNATURE")
    assert sig is None
    assert any("não encontrada" in msg for msg in caplog.messages)

def test_load_signature_file_json(tmp_path):
    # Cria arquivo JSON temporário com nova assinatura
    sig_file = tmp_path / "signatures.json"
    data = {
        "TEST_SIGNATURE": {
            "pattern": "dummy_pattern",
            "severity": "medium",
            "description": "Assinatura de teste"
        }
    }
    sig_file.write_text(json.dumps(data), encoding="utf-8")

    # Carrega assinaturas
    load_signature_file(str(sig_file))

    # Verifica se foi adicionada ao SIGNATURE_DB
    assert "TEST_SIGNATURE" in SIGNATURE_DB
    assert SIGNATURE_DB["TEST_SIGNATURE"]["severity"] == "medium"

def test_load_signature_file_invalid(tmp_path, caplog):
    # Cria arquivo inválido
    sig_file = tmp_path / "invalid.json"
    sig_file.write_text("[]", encoding="utf-8")  # lista em vez de dict

    load_signature_file(str(sig_file))

    # Deve logar erro de formato inválido
    assert any("Formato inválido" in msg for msg in caplog.messages)
