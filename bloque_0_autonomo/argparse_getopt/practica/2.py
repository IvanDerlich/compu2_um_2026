import sys

parser.add_argument(
    "entrada",
    nargs="?",  # opcional
    type=argparse.FileType('r'),
    default=sys.stdin,
    help="Archivo de entrada (default: stdin)"
)

parser.add_argument(
    "-o", "--output",
    type=argparse.FileType('w'),
    default=sys.stdout,
    help="Archivo de salida (default: stdout)"
)