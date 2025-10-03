#!/usr/bin/env python3
# 6_4.py - Guía 4 - Ejercicio 6
# Cargar vectores de cantidades y costos, calcular precios totales.

def main():
    n = int(input("Ingrese cantidad de productos: ").strip())
    cantidades = []
    costos = []
    for i in range(n):
        c = int(input(f"Ingrese cantidad del producto {i+1}: ").strip())
        costo = float(input(f"Ingrese costo unitario del producto {i+1}: ").strip())
        cantidades.append(c)
        costos.append(costo)
    for i in range(n):
        total = cantidades[i]*costos[i]
        print(f"Producto {i+1}: Cantidad {cantidades[i]}, Costo {costos[i]}, Total {total}")
        if total > 1000:
            print(f"El producto {i+1} supera los $1000 con total {total}")

if __name__ == '__main__':
    main()
