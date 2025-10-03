#!/usr/bin/env python3
# 4_5.py - Guía 5 - Ejercicio 4
# Cargar matriz 50x15 con ventas y encontrar el vendedor con mayor total.

def main():
    productos = 50
    vendedores = 15
    CANT = [[0 for _ in range(vendedores)] for _ in range(productos)]
    TOTAL = [0]*vendedores
    for i in range(productos):
        for j in range(vendedores):
            CANT[i][j] = int(input(f"Ingrese cantidad vendida del producto {i+1} por vendedor {j+1}: ").strip())
            TOTAL[j] += CANT[i][j]
    mayor = max(TOTAL)
    idx = TOTAL.index(mayor) + 1
    print(f"El vendedor que más vendió es el número {idx} con {mayor} artículos.")

if __name__ == '__main__':
    main()
