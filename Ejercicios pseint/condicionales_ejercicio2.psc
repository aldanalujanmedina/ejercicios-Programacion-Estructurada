Algoritmo condicionales_ejercicio2
	Definir mostacillas, canutillos, total Como Entero
	Imprimir "Ingrese el n�mero de bolsas de mostacillas que desea comprar"
	Leer mostacillas
	Imprimir "Ingrese el n�mero de canutillos que desea comprar"
	Leer canutillos
	
	total = mostacillas + canutillos 
	
	Si total < 5 imprimir "No se permiten compras inferiores a 5 productos."
	Sino Si total >= 5 & total <= 15 entonces imprimir "El costo de env�o es de $200" 
		Sino Si total > 15 entonces imprimir "El env�o es gratuito." 
				
			FinSi
		FinSi
		Finsi 
FinAlgoritmo
