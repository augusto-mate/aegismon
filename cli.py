# cli.py
import argparse
import json
import yaml
import sys
import os
from .scanner.core import Scanner
from .scanner.signatures import load_signature_file
from .reports.json_report import JSONReport # Classe JSONReport
from aegismon.logging.logger import get_logger

# Função auxiliar: carregar config YAML/JSON
def load_config(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {path}")
    with open(path, "r", encoding="utf-8") as f:
        if path.endswith(".yml") or path.endswith(".yaml"):
            return yaml.safe_load(f)
        elif path.endswith(".json"):
            return json.load(f)
        else:
            raise ValueError("Formato de configuração não suportado (use JSON ou YAML).")

# Comando: scan
def cmd_scan(args):
    # Logging
    logger = get_logger(level=args.log)
    
    # Config externa
    config = {}
    if args.config:
        logger.info(f"Carregando config: {args.config}")
        config = load_config(args.config)
    
    # Assinaturas externas
    if args.signatures:
        logger.info(f"Carregando assinaturas externas: {args.signatures}")
        load_signature_file(args.signatures)
    
    # Algoritmos de hashing
    algorithms = args.hashes or config.get("hashes") or ["md5", "sha1", "sha256"]
    
    scanner = Scanner(algorithms=algorithms)
    logger.info(f"Iniciando scan: {args.target}")
    
    # Chamada ao método scan_path do Scanner 
    result = scanner.scan_path(args.target)
    
    # Exportar JSON (usando JSONReport.export)
    if args.json:
        # A classe JSONReport e o método export devem ser usados 
        JSONReport.export(result, args.json)
        logger.info(f"Relatório JSON salvo em: {args.json}")
    
    # Verbose output
    if args.verbose:
        # Usando 'results' e 'stats' conforme a nova estrutura
        print(json.dumps(result, indent=2))
    
    return result

# Criação do CLI principal
def create_cli():
    parser = argparse.ArgumentParser(
        prog="aegismon",
        description="AegisMon — Scanner e Monitor de Segurança"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Subcomando: scan
    scan = subparsers.add_parser(
        "scan", help="Executa um scan em arquivo ou diretório"
    )
    scan.add_argument(
        "target", help="Arquivo ou diretório a ser analisado"
    )
    scan.add_argument(
        "--json", help="Exporta resultados para arquivo JSON"
    )
    scan.add_argument(
        "--log", choices=["info", "warning", "error", "debug"], 
        default="info", help="Nível de log"
    )
    scan.add_argument(
        "--hashes", nargs="+", help="Algoritmos de hashing (ex: md5 sha1 sha256)"
    )
    scan.add_argument(
        "--signatures", help="Carregar arquivo de assinaturas externas"
    )
    scan.add_argument(
        "--config", help="Arquivo de configuração YAML ou JSON"
    )
    scan.add_argument(
        "--verbose", action="store_true", help="Exibe saída completa no terminal"
    )
    scan.set_defaults(func=cmd_scan)
    return parser

# Ponto de entrada
def main():
    parser = create_cli()
    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    
    try:
        args.func(args)
    except Exception as e:
        print(f"[ERROR] {e}")
        return 1
    return 0

if __name__ == "__main__":

    sys.exit(main())
