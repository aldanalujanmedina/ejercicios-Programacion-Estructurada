print("Seleccione un número de acuerdo a su puesto de trabajo")
print("1. Repositor")
print("2. Cajero")
print("3. Supervisor")

op = int(input("Ingrese su opción: "))

if op == 1:
    print("Su sueldo en bruto es de 32335. Presione enter para saber más.")
    input()
    bruto1 = 32335
    jub1 = bruto1 * 0.11     
    os1 = bruto1 * 0.03      
    bono = bruto1 * 0.08     
    neto1 = bruto1 - jub1 - os1

    print("Su sueldo neto es", neto1)
    print("Sus deducciones son", jub1, "por jubilación y", os1, "por obra social")
    print("Se le informa que obtuvo un bono de", bono)

elif op == 2:
    print("Su sueldo en bruto es de 38630.89. Presione enter para saber más.")
    input()
    bruto2 = 38630.89
    jub2 = bruto2 * 0.11
    os2 = bruto2 * 0.03
    neto2 = bruto2 - jub2 - os2

    print("Su sueldo neto es", neto2)
    print("Sus deducciones son", jub2, "por jubilación y", os2, "por obra social")

elif op == 3:
    print("Su sueldo en bruto es de 45560.20. Presione enter para saber más.")
    input()
    bruto3 = 45560.20
    jub3 = bruto3 * 0.11
    os3 = bruto3 * 0.03
    neto3 = bruto3 - jub3 - os3

    print("Su sueldo neto es", neto3)
    print("Sus deducciones son", jub3, "por jubilación y", os3, "por obra social")

else:
    print("Error. Seleccione un número del 1 al 3 de acuerdo a su puesto de trabajo")
