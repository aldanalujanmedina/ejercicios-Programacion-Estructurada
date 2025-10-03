#!/usr/bin/env python3
# 1_4.py - Guía 4 - Ejercicio 1
# Cargar n notas en un vector, mostrar la más alta y el promedio.

def main():
    n = int(input("Ingrese la cantidad de notas: ").strip())
    notas = []
    for i in range(n):
        nota = float(input(f"Ingrese la nota {i+1}: ").strip())
        notas.append(nota)
    mayor = max(notas)
    promedio = sum(notas)/n if n > 0 else 0
    print(f"Nota más alta: {mayor}")
    print(f"Promedio: {promedio:.2f}")

if __name__ == '__main__':
    main()
