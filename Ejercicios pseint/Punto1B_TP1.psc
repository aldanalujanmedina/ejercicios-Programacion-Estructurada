Algoritmo Punto1B_TP1
	Definir edad Como Entero
	Imprimir "Indique su edad"
	Leer edad
	
	Escribir "Indique el número correspondiente de acuerdo a su sexo."
	Escribir "1. Mujer"
	Escribir "2. Hombre"
	Leer OP
	
	Según OP hacer 
1: SI edad >= 16 Entonces
		Imprimir "Usted es mujer y puede votar."
		Sino imprimir "Usted es mujer y no puede votar."
		FinSi
2: SI edad >= 16 Entonces
		Imprimir "Usted es hombre y puede votar."
	    Sino imprimir "Usted es hombre y no puede votar."
		FinSi
FinSegun

FinAlgoritmo
