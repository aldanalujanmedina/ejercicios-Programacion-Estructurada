Algoritmo Guia5ejercicio3
	Definir matriznotas Como Entero
	Definir promedio Como Real
	Dimensión matriznotas[40,5]
	Dimensión promedio[40] //vector donde se guardan los promedios
	Definir fil Como Entero
	//recorrer la matriz notas
	para fil=0 hasta 39 Hacer
		Para col=0 hasta 4 Hacer
			matriznotas[fil,col] = Aleatorio(1,10)
			Imprimir Sin Saltar matriznotas[fil,col], " "
		FinPara
		Imprimir " "
	FinPara

FinAlgoritmo
