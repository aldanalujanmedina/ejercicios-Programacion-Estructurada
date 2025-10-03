#!/usr/bin/env python3
# 1_5.py - Guía 5 - Ejercicio 1
# Generar una matriz 4x4 rellena de ceros y mostrarla.

def main():
    matriz = [[0 for _ in range(4)] for _ in range(4)]
    for fila in matriz:
        print(fila)

if __name__ == '__main__':
    main()
