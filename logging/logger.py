# aegismon/logging/logger.py
import logging
import sys

def get_logger(name="aegismon", level="INFO"):
    """
    Configura e retorna um logger centralizado.
    """
    # Converter nível de string para constante
    log_level = getattr(logging, level.upper(), logging.INFO)
    
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Evitar adicionar múltiplos handlers se já estiver configurado
    if not logger.handlers:
        # Formato de log
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] (%(name)s): %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Handler para saída padrão (stdout)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger