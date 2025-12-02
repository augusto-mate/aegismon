# aegismon/scanner/__init__.py
"""
Scanner package: fornece classes e funções para análise de arquivos,
incluindo assinaturas, heurísticas e múltiplos algoritmos de hashing.
"""

from .core import Scanner, ScanResult
from .signatures import SIGNATURE_DB, get_signature, load_signature_file
