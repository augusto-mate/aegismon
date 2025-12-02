# aegismon/scanner/signatures.py
"""
Signatures module: mantém a base de assinaturas usadas pelo scanner.
"""

import json
import yaml
from pathlib import Path
from ..logger import get_logger

logger = get_logger(__name__)

SIGNATURE_DB = {
    "EICAR_TEST_FILE": {
        "pattern": "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*",
        "severity": "low",
        "description": "Arquivo de teste EICAR"
    }
}

def get_signature(name: str):
    sig = SIGNATURE_DB.get(name)
    if sig:
        logger.debug(f"Signature '{name}' encontrada: {sig}")
    else:
        logger.warning(f"Signature '{name}' não encontrada.")
    return sig

def load_signature_file(path: str):
    """
    Carrega assinaturas de um arquivo JSON ou YAML e atualiza SIGNATURE_DB.
    """
    file = Path(path)
    if not file.exists():
        logger.error(f"Arquivo de assinaturas não encontrado: {path}")
        return

    try:
        if file.suffix.lower() in [".yaml", ".yml"]:
            with open(file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        else:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

        if isinstance(data, dict):
            SIGNATURE_DB.update(data)
            logger.info(f"{len(data)} assinaturas carregadas de {path}")
        else:
            logger.error(f"Formato inválido em {path}: esperado dict, obtido {type(data)}")

    except Exception as e:
        logger.exception(f"Erro ao carregar assinaturas de {path}: {e}")

