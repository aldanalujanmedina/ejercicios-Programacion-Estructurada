#!/usr/bin/env python3
# 2_4.py - Guía 4 - Ejercicio 2
# Contar aprobados y desaprobados en un vector de n notas.

def main():
    n = int(input("Ingrese la cantidad de notas: ").strip())
    notas = []
    for i in range(n):
        nota = float(input(f"Ingrese la nota {i+1}: ").strip())
        notas.append(nota)
    aprobados = sum(1 for x in notas if x >= 6)
    desaprobados = n - aprobados
    print(f"Aprobados: {aprobados}, Desaprobados: {desaprobados}")

if __name__ == '__main__':
    main()
