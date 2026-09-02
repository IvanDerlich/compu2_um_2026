# python3 5.py init oaeua
# Inicializando oaeua
# python3 5.py build
# Compilando en modo debug
# python3 5.py build --release
# Compilando en modo release

import argparse

parser = argparse.ArgumentParser(prog="mi-herramienta")
subparsers = parser.add_subparsers(dest="comando")

# Subcomando: init
parser_init = subparsers.add_parser("init", help="Inicializar proyecto")
parser_init.add_argument("nombre", help="Nombre del proyecto")

# Subcomando: build
parser_build = subparsers.add_parser("build", help="Compilar")
parser_build.add_argument("--release", action="store_true")

args = parser.parse_args()

if args.comando == "init":
    print(f"Inicializando {args.nombre}")
elif args.comando == "build":
    print(f"Compilando en modo {'release' if args.release else 'debug'}")