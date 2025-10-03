#!/usr/bin/env python3
# 4_4.py - Guía 4 - Ejercicio 4
# Cargar edades de 20 personas y mostrar promedio y la más joven.

def main():
    edades = []
    for i in range(20):
        edad = int(input(f"Ingrese edad de la persona {i+1}: ").strip())
        edades.append(edad)
    promedio = sum(edades)/len(edades)
    joven = min(edades)
    print(f"Promedio de edad: {promedio:.2f}")
    print(f"La persona más joven tiene: {joven} años")

if __name__ == '__main__':
    main()
