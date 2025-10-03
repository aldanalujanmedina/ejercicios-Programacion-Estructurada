#!/usr/bin/env python3
# 8_3.py - Guía 3 - Ejercicio 8
# Procesa datos de un censo.

def main():
    total = 0
    varones = 0
    mujeres = 0
    varones_16_65 = 0
    mayor_edad = -1
    persona_mayor = None
    while True:
        doc = input("Número de documento (0 para terminar): ").strip()
        if doc == "0":
            break
        edad = int(input("Edad: ").strip())
        sexo = input("Sexo (M/F): ").strip().upper()
        total += 1
        if sexo == "M":
            varones += 1
            if 16 <= edad <= 65:
                varones_16_65 += 1
        elif sexo == "F":
            mujeres += 1
        if edad > mayor_edad:
            mayor_edad = edad
            persona_mayor = (doc, edad, sexo)
    print(f"Cantidad total censada: {total}")
    print(f"Cantidad de varones: {varones}")
    print(f"Cantidad de mujeres: {mujeres}")
    if varones > 0:
        porcentaje = (varones_16_65/varones)*100
        print(f"Porcentaje de varones entre 16 y 65 años: {porcentaje:.2f}%")
    if persona_mayor:
        print(f"Persona de mayor edad: DNI {persona_mayor[0]}, Edad {persona_mayor[1]}, Sexo {persona_mayor[2]}")

if __name__ == '__main__':
    main()
