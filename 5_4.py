#!/usr/bin/env python3
# 5_4.py - Guía 4 - Ejercicio 5
# Vendedores y ventas, mostrar mayor, menor y convertir a pesos.

def main():
    vendedores = []
    ventas = []
    for i in range(15):
        nombre = input(f"Ingrese nombre del vendedor {i+1}: ").strip()
        monto = float(input(f"Ingrese ventas en dólares de {nombre}: ").strip())
        vendedores.append(nombre)
        ventas.append(monto)
    mayor = max(ventas)
    menor = min(ventas)
    idx_mayor = ventas.index(mayor)
    idx_menor = ventas.index(menor)
    print(f"Mayor venta: {vendedores[idx_mayor]} con ${ventas[idx_mayor]} USD / ${ventas[idx_mayor]*140} ARS")
    print(f"Menor venta: {vendedores[idx_menor]} con ${ventas[idx_menor]} USD / ${ventas[idx_menor]*140} ARS")

if __name__ == '__main__':
    main()
