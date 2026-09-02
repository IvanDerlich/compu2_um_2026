import argparse

parser = argparse.ArgumentParser(description="Procesa un archivo de texto")
parser.add_argument("entrada", help="Archivo de entrada")
parser.add_argument("salida", help="Archivo de salida")
parser.add_argument("-v", "--verbose", action="store_true", help="Modo detallado")
parser.add_argument("-o", "--output", default="salida.txt", help="Archivo de salida")
parser.add_argument("-n", "--numero", type=int, default=10, help="Cantidad")

args = parser.parse_args()

print(f"Procesando {args.archivo}")
print(f"Verbose: {args.verbose}")
print(f"Líneas: {args.lineas}")