#!/usr/bin/env python3
# 6_3.py - Guía 3 - Ejercicio 6
# Calcula el menor tiempo en carrera de 12 competidores.

def main():
    mejor_tiempo = None
    mejor_auto = None
    for _ in range(12):
        auto = input("Número de vehículo: ").strip()
        try:
            tiempo = float(input("Tiempo en segundos: ").strip())
        except Exception:
            print("Tiempo inválido.")
            continue
        if mejor_tiempo is None or tiempo < mejor_tiempo:
            mejor_tiempo = tiempo
            mejor_auto = auto
    if mejor_auto is not None:
        print(f"El mejor tiempo lo hizo el vehículo {mejor_auto} con {mejor_tiempo} segundos.")
    else:
        print("No se registraron tiempos válidos.")

if __name__ == '__main__':
    main()
