import argparse

parser = argparse.ArgumentParser(description="Ejemplo de niveles de verbosidad")

parser.add_argument(
    "-v", "--verbose",
    action="count",
    default=0,
    help="Aumentar verbosidad (-v, -vv, -vvv)"
)

args = parser.parse_args()

# Después:
if args.verbose >= 3:
    print("Debug: detalle fino")
elif args.verbose >= 2:
    print("Warning: posibles problemas")
elif args.verbose >= 1:
    print("Info: operación normal")
else:
    print("Modo silencioso")