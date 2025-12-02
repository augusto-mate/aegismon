# aegismon/scanner/__init__.py
"""
Scanner package: fornece classes e funções para análise de arquivos,
incluindo assinaturas, heurísticas e múltiplos algoritmos de hashing.
"""

""" Inicialização do pacote scanner. """

# Importa os principais componentes para fácil acesso
# Certifique-se que o .signatures é importado antes de .core se houver dependências.
from .signatures import load_signature_file, SIGNATURE_DB
from .core import Scanner, ScanResult 

__all__ = [
    'Scanner',
    'ScanResult',
    'load_signature_file',
    'SIGNATURE_DB'
]
