# aegismon/scanner/signatures.py
"""
Signatures module: mantém a base de assinaturas usadas pelo scanner.
"""

from ..logger import get_logger   # corrigido: antes era ..logging.logger

# Instância de logger para este módulo
logger = get_logger(__name__)

# Base de assinaturas (exemplo inicial, pode ser expandida futuramente)
SIGNATURE_DB = {
    "EICAR_TEST_FILE": {
        "pattern": "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*",
        "severity": "low",
        "description": "Arquivo de teste EICAR"
    },
    "MALWARE_SAMPLE": {
        "pattern": "malicious_code_signature",
        "severity": "high",
        "description": "Assinatura genérica de malware"
    }
}

def get_signature(name: str):
    """
    Retorna uma assinatura pelo nome, ou None se não existir.
    """
    sig = SIGNATURE_DB.get(name)
    if sig:
        logger.debug(f"Signature '{name}' encontrada: {sig}")
    else:
        logger.warning(f"Signature '{name}' não encontrada.")
    return sig
