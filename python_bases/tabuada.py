#!/usr/bin/env python3
"""Imprime a tabuada de 1 ao 10"""
__version__ = "0.1.0"
__author__ = "Victor Pitangui"

numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-------------")

