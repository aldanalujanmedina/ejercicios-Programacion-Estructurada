#!/usr/bin/env python3
# 1_2.py - Guía 2 - Ejercicio 1
# Calcula sueldo neto según categoría y muestra descuentos. Para repositores muestra bono de compra (8%).

def main():
    sueldos = {1: 32335.0, 2: 38630.89, 3: 45560.20}
    try:
        tipo = int(input("Ingrese el tipo de empleado (1-repositor, 2-cajero, 3-supervisor): ").strip())
    except Exception:
        print("Entrada inválida. Debe ingresar 1, 2 o 3.")
        return
    if tipo not in sueldos:
        print("Tipo de empleado inválido. Debe ser 1, 2 o 3.")
        return
    bruto = sueldos[tipo]
    porc_jub = 0.11
    porc_obra = 0.03
    descuento_jub = bruto * porc_jub
    descuento_obra = bruto * porc_obra
    neto = bruto - descuento_jub - descuento_obra
    categorias = {1: "Repositor", 2: "Cajero", 3: "Supervisor"}
    print(f"Categoría: {categorias[tipo]}")
    print(f"Sueldo bruto: ${bruto:.2f}")
    print(f"Descuento Jubilación (11%): ${descuento_jub:.2f}")
    print(f"Descuento Obra Social (3%): ${descuento_obra:.2f}")
    print(f"Sueldo neto: ${neto:.2f}")
    if tipo == 1:
        bono = bruto * 0.08
        print(f"Bono en compras (8% del sueldo): ${bono:.2f}")

if __name__ == '__main__':
    main()
