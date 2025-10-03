#!/usr/bin/env python3
# 7_4.py - Guía 4 - Ejercicio 7
# Control de egreso de 30 camiones y contar los que llevan té.

def main():
    camiones = []
    contador_te = 0
    for i in range(30):
        patente = input("Patente del camión: ").strip()
        chofer = input("Nombre y apellido del chofer: ").strip()
        carga = input("Tipo de carga (madera/yerba/te): ").strip().lower()
        hora = input("Hora de egreso: ").strip()
        if carga == "te":
            contador_te += 1
        camiones.append((patente, chofer, carga, hora))
    print("Datos de camiones:")
    for c in camiones:
        print(c)
    print(f"Cantidad de camiones que transportan té: {contador_te}")

if __name__ == '__main__':
    main()
