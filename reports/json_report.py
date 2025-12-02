# aegismon/reports/json_report.py
import json
from aegismon.logging.logger import get_logger

logger = get_logger(__name__)

class JSONReport:
    """
    Classe utilitária para exportar resultados de scan para JSON.
    """
    @staticmethod
    def export(data, filepath):
        """
        Salva o dicionário de resultados em um arquivo JSON.
        """
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logger.info(f"Relatório JSON salvo com sucesso em: {filepath}")
        except IOError as e:
            logger.error(f"Erro ao salvar relatório JSON em {filepath}: {e}")

            raise
            
