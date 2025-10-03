#!/usr/bin/env python3
# 2_2.py - Guía 2 - Ejercicio 2
# Control de cantidad de paquetes y costo de envío.

def main():
    try:
        cantidad = int(input("Ingrese la cantidad de paquetes comprados: ").strip())
    except Exception:
        print("Entrada inválida. Ingrese un número entero.")
        return
    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return
    if cantidad < 5:
        print("No se permiten compras inferiores a 5 productos.")
    elif 5 <= cantidad <= 15:
        print("El costo de envío es de $200.")
    else:
        print("El envío es gratuito.")

if __name__ == '__main__':
    main()
