#!/usr/bin/env python3
# 2_5.py - Guía 5 - Ejercicio 2
# Generar matriz 4x4 con diagonal en 1 y el resto 0.

def main():
    n = 4
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matriz[i][n-1-i] = 1
    for fila in matriz:
        print(fila)

if __name__ == '__main__':
    main()
