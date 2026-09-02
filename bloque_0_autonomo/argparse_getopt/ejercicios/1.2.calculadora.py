#!/usr/bin/env python3

import sys

numeros = [float(numero) for numero in sys.argv[1:]]
resultado = sum(numeros)

print(f"Suma: {resultado}")