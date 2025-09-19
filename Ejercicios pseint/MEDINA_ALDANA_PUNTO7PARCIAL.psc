Algoritmo MEDINA_ALDANA_PUNTO7PARCIAL
		Definir numero, mayor, menor Como Entero
		Definir  numero1 Como Logico
		numero1 = Falso
		Escribir "Por favor ingrese los números. Para finalizar, ingrese -1"
		Leer numero
		
		Mientras numero <> -1 Hacer
			Si numero < 0 Entonces
				Escribir "Error: ingresó un valor no permitido. Intente de nuevo."
			Sino
				Si numero1 = Falso Entonces
					mayor=numero
					menor=numero
					numero1 = Verdadero
				Sino
					Si numero > mayor Entonces
						mayor = numero
						menor = numero 
					FinSi
					Si numero < menor Entonces
						menor = numero
					FinSi
				FinSi
			FinSi
			
			Leer numero
		FinMientras
		
		Si numero1 = Verdadero Entonces
			Escribir "El mayor valor ingresado es: ", mayor
			Escribir "El menor valor ingresado es: ", menor
		Sino
			Escribir "No se ingresaron números válidos en la secuencia."
		FinSi
		
FinAlgoritmo
