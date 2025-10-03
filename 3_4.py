#!/usr/bin/env python3
# 3_4.py - Guía 4 - Ejercicio 3
# Cargar sueldos de 10 empleados y mostrar el mayor.

def main():
    sueldos = []
    for i in range(10):
        sueldo = float(input(f"Ingrese sueldo del empleado {i+1}: ").strip())
        sueldos.append(sueldo)
    mayor = max(sueldos)
    print("Sueldos ingresados:")
    for s in sueldos:
        print(s)
    print(f"El mayor sueldo es: {mayor}")

if __name__ == '__main__':
    main()
