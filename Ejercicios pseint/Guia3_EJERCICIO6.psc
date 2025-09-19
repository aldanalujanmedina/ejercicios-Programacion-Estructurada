Algoritmo Guia3_EJERCICIO6
	Definir menor_valor,tiempo_segundos Como Entero
	Definir vehiculoconmenortiempo Como Caracter
	menor_valor=999999
	
	Para i=1 hasta 12 Con Paso 1 Hacer
		
		imprimir "vehículo"
		leer vehículo
		
		Imprimir "tiempo_segundos"
		leer tiempo_segundos
		
		si tiempo_segundos < menor_valor Entonces
			menor_valor=tiempo_segundos
			vehiculoconmenortiempo = vehículo 
		FinSi
		
	FinPara
	
	Imprimir "El vehículo con menor tiempo es", vehículoconmenortiempo
	Imprimir "Su menor tiempo es", menor_valor
	
FinAlgoritmo
