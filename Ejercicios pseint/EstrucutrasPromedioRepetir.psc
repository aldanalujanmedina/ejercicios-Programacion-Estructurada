Algoritmo EstrucutrasPromedioRepetir
	Definir edad Como Entero
	Definir acumulador Como Entero
	Definir contadordealumnos Como Entero
	Definir promedio Como Real

	Repetir
		flag = Verdadero
		Escribir "Ingrese la edad del alumno: "
		Leer edad
		Escribir "La edad es :", edad
		Si edad > 1 Entonces
			contadordealumnos + 1
		
		FinSi
		acumulador + edad
	Hasta Que edad = 0 
	flag = Verdadero
	
	
	promedio = acumulador + contadordealumnos
FinAlgoritmo


