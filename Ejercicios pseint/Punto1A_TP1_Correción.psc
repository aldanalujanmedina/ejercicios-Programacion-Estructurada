Algoritmo Punto1A_TP1_Correci�n
	Definir radio Como Real
	Definir L1, L2, L3, L4, L5 Como Entero
	Definir Base, Altura Como Entero
	Definir OP Como Entero
	
	Escribir "Seleccione un n�mero de acuerdo a la acci�n que desea realizar."
	Escribir "1. El per�metro y �rea de un c�rculo dado su radio."
	Escribir "2. El �rea y per�metro de un pent�gono."
	Escribir "3. El per�metro y �rea de un rect�ngulo."
	Leer OP
	
	Si OP = 1 Entonces
		Escribir "Indique el radio de su c�rculo."
		Leer radio
		P1 = 2 * PI * radio
		A1 = PI * (radio^2)
		Escribir "El per�metro de su c�rculo es " P1 " y su �rea es " A1
		
	Sino
		Si OP = 2 Entonces
			Escribir "Indique las longitudes de los 5 lados de su pent�gono (en cent�metros)"
			Leer L1, L2, L3, L4, L5
			P2 = L1 + L2 + L3 + L4 + L5
			Apotema = L1 / (2 * tan(0.2*PI))
			A2 = (P2 * Apotema) / 2
			Escribir "El per�metro de su pent�gono es " P2 " y su �rea es " A2
			
		Sino
			Si OP = 3 Entonces
				Escribir "Indique la base de su rect�ngulo"
				Leer Base
				Escribir "Indique la altura de su rect�ngulo"
				Leer Altura 
				P3 = 2 * (Base + Altura) 
				A3 = Base * Altura
				Escribir "El per�metro de su rect�ngulo es " P3 " y el �rea de su rect�ngulo es " A3
			Sino
				Escribir "ERROR. Elija un n�mero del 1 al 3."
			FinSi
		FinSi
	FinSi
FinAlgoritmo

