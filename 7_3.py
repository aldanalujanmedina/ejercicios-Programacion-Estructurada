#!/usr/bin/env python3
# 7_3.py - Guía 3 - Ejercicio 7
# Registro de socios por deporte y promedio de edad.

def main():
    deportes = {1: "Tenis", 2: "Rugby", 3: "Voley", 4: "Hockey", 5: "Futbol"}
    conteo = {d: 0 for d in deportes}
    suma_edades = {d: 0 for d in deportes}
    cantidad_socios = int(input("Ingrese la cantidad de socios a registrar: "))
    for _ in range(cantidad_socios):
        nro = input("Número de socio: ").strip()
        edad = int(input("Edad: ").strip())
        tipo = int(input("Deporte (1-tenis,2-rugby,3-voley,4-hockey,5-futbol): ").strip())
        if tipo in deportes:
            conteo[tipo] += 1
            suma_edades[tipo] += edad
    print(f"Cantidad de socios en Tenis: {conteo[1]}")
    print(f"Cantidad de socios en Futbol: {conteo[5]}")
    for t in deportes:
        if conteo[t] > 0:
            promedio = suma_edades[t]/conteo[t]
            print(f"Promedio de edad en {deportes[t]}: {promedio:.2f}")

if __name__ == '__main__':
    main()
