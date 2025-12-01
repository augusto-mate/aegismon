# aegismon/scanner/signatures.py
import json
import os
from ..logging.logger import get_logger

logger = get_logger(__name__)

# Banco de dados de assinaturas global
SIGNATURE_DB = {
    # Exemplo de assinatura do arquivo de teste EICAR
    "EICAR_Test_File": {
        "md5": "44d88612fea8a8f36de82e1278abb02f",
        "sha1": "3395856ce81f2b7382dee72602f798b6c430e1d1",
        "sha256": "275a021aa907954e74e471f6607204f131a4038a37951a8048ed33857e43685f"
    },
    "Demo_Malware_1": {
        "md5": "a1b2c3d4e5f600112233445566778899"
    }
}

def load_signature_file(filepath):
    """
    Carrega assinaturas de um arquivo JSON externo e as mescla 
    no banco de dados global (SIGNATURE_DB).
    """
    global SIGNATURE_DB
    
    if not os.path.exists(filepath):
        logger.warning(f"Arquivo de assinaturas não encontrado: {filepath}")
        return
        
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            external_signatures = json.load(f)
            
        # Mesclar novas assinaturas
        SIGNATURE_DB.update(external_signatures)
        logger.info(f"{len(external_signatures)} assinaturas externas carregadas.")
        
    except json.JSONDecodeError:
        logger.error(f"Erro ao decodificar JSON em {filepath}.")
    except Exception as e:
        logger.error(f"Erro ao carregar arquivo de assinaturas: {e}")