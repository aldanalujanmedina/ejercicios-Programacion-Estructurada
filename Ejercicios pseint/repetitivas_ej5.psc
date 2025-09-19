Algoritmo repetitivas_ej5
    Definir dni, servicio, monto Como Entero
    Para i <- 1 Hasta 5 Hacer
        Escribir "Ingrese DNI del cliente:"
        Leer dni
        Escribir "Ingrese tipo de servicio (1=30mb, 2=50mb, 3=100mb):"
        Leer servicio
        Segun servicio Hacer
            1:
                monto <- 750
            2:
                monto <- 1100
            3:
                monto <- 1500 * 0.95
        FinSegun
        Escribir "Cliente DNI:", dni, " Servicio:", servicio, " Monto a pagar:", monto
    FinPara
FinAlgoritmo

