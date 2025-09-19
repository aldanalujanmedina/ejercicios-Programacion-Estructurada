Algoritmo condicionales_ejercicio2
	Definir mostacillas, canutillos, total Como Entero
	Imprimir "Ingrese el número de bolsas de mostacillas que desea comprar"
	Leer mostacillas
	Imprimir "Ingrese el número de canutillos que desea comprar"
	Leer canutillos
	
	total = mostacillas + canutillos 
	
	Si total < 5 imprimir "No se permiten compras inferiores a 5 productos."
	Sino Si total >= 5 & total <= 15 entonces imprimir "El costo de envío es de $200" 
		Sino Si total > 15 entonces imprimir "El envío es gratuito." 
				
			FinSi
		FinSi
		Finsi 
FinAlgoritmo
