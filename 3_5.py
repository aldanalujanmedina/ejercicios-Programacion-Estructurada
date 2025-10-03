#!/usr/bin/env python3
# 3_5.py - Guía 5 - Ejercicio 3
# Calcular promedio de 5 notas por 40 alumnos en matriz 40x5.

def main():
    alumnos = 40
    notas = 5
    matriz = []
    for i in range(alumnos):
        fila = []
        for j in range(notas):
            n = float(input(f"Ingrese nota {j+1} del alumno {i+1}: ").strip())
            fila.append(n)
        matriz.append(fila)
    for i in range(alumnos):
        promedio = sum(matriz[i])/notas
        print(f"Alumno {i+1}, Promedio: {promedio:.2f}")

if __name__ == '__main__':
    main()
