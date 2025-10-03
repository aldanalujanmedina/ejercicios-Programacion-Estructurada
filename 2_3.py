#!/usr/bin/env python3
# 2_3.py - Guía 3 - Ejercicio 2
# Pide un límite numérico y muestra todos los números desde 1 hasta el límite.

def main():
    try:
        limite = int(input("Ingrese el límite numérico: ").strip())
    except Exception:
        print("Entrada inválida. Debe ser un número entero.")
        return
    for i in range(1, limite + 1):
        print(i)

if __name__ == '__main__':
    main()
