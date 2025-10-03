#!/usr/bin/env python3
# 3_2.py - Guía 2 - Ejercicio 3
# Calcula montos por producto, total y aplica descuento del 10% si corresponde.

def pedir_numero(prompt):
    while True:
        try:
            v = input(prompt).strip()
            if v == '':
                return 0.0
            return float(v)
        except ValueError:
            print("Entrada inválida. Ingrese un número (ej: 12.5).")

def main():
    print("Ingrese precio por Kg y cantidad en Kg para 3 productos.")
    precios = []
    kgs = []
    for i in range(1,4):
        p = pedir_numero(f"Precio por Kg del producto {i}: ")
        q = pedir_numero(f"Cantidad (Kg) del producto {i}: ")
        precios.append(p)
        kgs.append(q)
    montos = [precios[i]*kgs[i] for i in range(3)]
    for i,m in enumerate(montos, start=1):
        print(f"Monto producto {i}: ${m:.2f}")
    total = sum(montos)
    print(f"Total antes de descuento: ${total:.2f}")
    if total > 100:
        descuento = total * 0.10
        nuevo_total = total - descuento
        print("Se aplica descuento del 10% porque el total es superior a $100.")
        print(f"Descuento: ${descuento:.2f}")
        print(f"Nuevo monto a pagar: ${nuevo_total:.2f}")
    else:
        print("No corresponde descuento.")

if __name__ == '__main__':
    main()
