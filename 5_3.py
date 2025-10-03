#!/usr/bin/env python3
# 5_3.py - Guía 3 - Ejercicio 5
# Calcula monto a pagar por servicio de internet de 5 clientes.

def main():
    precios = {1: 750, 2: 1100, 3: 1500}
    for _ in range(5):
        dni = input("Ingrese DNI del cliente: ").strip()
        try:
            tipo = int(input("Ingrese tipo de servicio (1-30MB, 2-50MB, 3-100MB): ").strip())
        except Exception:
            print("Tipo de servicio inválido.")
            continue
        if tipo not in precios:
            print("Servicio no válido.")
            continue
        monto = precios[tipo]
        if tipo == 3:
            monto *= 0.95  # 5% de descuento
        print(f"DNI: {dni}, Servicio: {tipo}, Monto a pagar: ${monto:.2f}")

if __name__ == '__main__':
    main()
