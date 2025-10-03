#!/usr/bin/env python3
# 4_2.py - Guía 2 - Ejercicio 4
# Calcula sueldo neto según categoría, muestra DNI y nombre de categoría.

def main():
    dni = input("Ingrese el DNI del empleado: ").strip()
    try:
        categoria = int(input("Ingrese la categoría (0-Maestranza, 1-Administración, 2-Gerencia): ").strip())
    except Exception:
        print("Entrada inválida. La categoría debe ser 0, 1 o 2.")
        return
    categorias = {
        0: ("Maestranza", 23600.0, 0.11, 0.03, 0.0),   # (nombre, bruto, jub, obra, club)
        1: ("Administración", 35800.0, 0.11, 0.05, 0.0),
        2: ("Gerencia", 60420.0, 0.11, 0.05, 0.04)
    }
    if categoria not in categorias:
        print("Categoría inválida. Debe ser 0, 1 o 2.")
        return
    nombre, bruto, pct_jub, pct_obra, pct_club = categorias[categoria]
    desc_jub = bruto * pct_jub
    desc_obra = bruto * pct_obra
    desc_club = bruto * pct_club
    neto = bruto - (desc_jub + desc_obra + desc_club)
    print(f"DNI: {dni}")
    print(f"Categoría: {nombre}")
    print(f"Sueldo bruto: ${bruto:.2f}")
    print(f"Descuento Jubilación ({pct_jub*100:.0f}%): ${desc_jub:.2f}")
    print(f"Descuento Obra Social ({pct_obra*100:.0f}%): ${desc_obra:.2f}")
    if pct_club > 0:
        print(f"Descuento Club ({pct_club*100:.0f}%): ${desc_club:.2f}")
    print(f"Sueldo neto: ${neto:.2f}")

if __name__ == '__main__':
    main()
