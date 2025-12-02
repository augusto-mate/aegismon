# aegismon/scanner/__init__.py
""" Inicialização do pacote scanner. """

# Importa os principais componentes para fácil acesso
from .core import Scanner, ScanResult
from .signatures import load_signature_file, SIGNATURE_DB

__all__ = [
    'Scanner',
    'ScanResult',
    'load_signature_file',
    'SIGNATURE_DB'

]
