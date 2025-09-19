Algoritmo condicionalesejercicio1
	Escribir "Seleccione un número de acuerdo a su puesto de trabajo"
	Escribir "1. Repositor"
	Escribir "2. Cajero"
	Escribir "3. Supervisor"
	Leer OP
	Según OP hacer 
	1: Escribir "Su sueldo en bruto es de 32335. Presione enter para saber más."
		Bruto1= 32335
		Jub1 = Bruto1 - 0.11
		OS1 = Bruto1 - 0.03
		Bono = Bruto1 + 0.08
		Neto1 = Bruto1 - Jub1 - OS1 
		Esperar Tecla
		Escribir "Su sueldo neto es " Neto1
		Escribir "Sus deducciones son " Jub1 " por jubilación y " OS1 " por obra social"
		Escribir "Se le informa que obtuvo un bono de " Bono
	2:  Escribir "Su sueldo en bruto es de 38630,89. Presione enter para saber más."
		Bruto2= 38630.89
		Jub2 = Bruto2 - (Bruto2 - 11/100)
		OS2 = Bruto2- (Bruto2 - 3/100)
		Neto2 = Bruto2 - Jub2 - OS2 
		Esperar Tecla
		Escribir "Su sueldo neto es " Neto2
		Escribir "Sus deducciones son " Jub2 " por jubilación y " OS2 " por obra social"
	3:  Escribir "Su sueldo en bruto es de 45560,20. Presione enter para saber más."
		Bruto3= 45560.20
		Jub3 = Bruto3 - (Bruto3 - 11/100)
		OS3 = Bruto3- (Bruto3 - 3/100)
		Neto3 = Bruto3 - Jub3 - OS3
		Esperar Tecla
		Escribir "Su sueldo neto es " Neto3
		Escribir "Sus deducciones son " Jub3 " por jubilación y " OS3 " por obra social"
FinSegun
FinAlgoritmo
