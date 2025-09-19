Algoritmo Punto1A_TP1_Correción
	Definir radio Como Real
	Definir L1, L2, L3, L4, L5 Como Entero
	Definir Base, Altura Como Entero
	Definir OP Como Entero
	
	Escribir "Seleccione un número de acuerdo a la acción que desea realizar."
	Escribir "1. El perímetro y área de un círculo dado su radio."
	Escribir "2. El área y perímetro de un pentágono."
	Escribir "3. El perímetro y área de un rectángulo."
	Leer OP
	
	Si OP = 1 Entonces
		Escribir "Indique el radio de su círculo."
		Leer radio
		P1 = 2 * PI * radio
		A1 = PI * (radio^2)
		Escribir "El perímetro de su círculo es " P1 " y su área es " A1
		
	Sino
		Si OP = 2 Entonces
			Escribir "Indique las longitudes de los 5 lados de su pentágono (en centímetros)"
			Leer L1, L2, L3, L4, L5
			P2 = L1 + L2 + L3 + L4 + L5
			Apotema = L1 / (2 * tan(0.2*PI))
			A2 = (P2 * Apotema) / 2
			Escribir "El perímetro de su pentágono es " P2 " y su área es " A2
			
		Sino
			Si OP = 3 Entonces
				Escribir "Indique la base de su rectángulo"
				Leer Base
				Escribir "Indique la altura de su rectángulo"
				Leer Altura 
				P3 = 2 * (Base + Altura) 
				A3 = Base * Altura
				Escribir "El perímetro de su rectángulo es " P3 " y el área de su rectángulo es " A3
			Sino
				Escribir "ERROR. Elija un número del 1 al 3."
			FinSi
		FinSi
	FinSi
FinAlgoritmo

