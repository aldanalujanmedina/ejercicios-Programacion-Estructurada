#!/usr/bin/env python3
# 5_5.py - Guía 5 - Ejercicio 5
# Guardar notas de 4 alumnos (3 notas y promedio en la 4ta columna).

def main():
    filas = 4
    cols = 4
    matriz = [[0 for _ in range(cols)] for _ in range(filas)]
    for i in range(filas):
        suma = 0
        for j in range(3):
            nota = float(input(f"Ingrese nota {j+1} del alumno {i+1}: ").strip())
            matriz[i][j] = nota
            suma += nota
        matriz[i][3] = suma/3
    print("Notas y promedios:")
    for i in range(filas):
        print(f"Alumno {i+1}: Notas {matriz[i][0:3]}, Promedio {matriz[i][3]:.2f}")

if __name__ == '__main__':
    main()
