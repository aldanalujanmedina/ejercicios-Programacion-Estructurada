Algoritmo EstrucutrasPromedioMientras
	Definir edad Como Entero
	Definir acuml_edad Como Entero
	Definir contadorAlumno Como Entero
	Definir promedio Como Real
	Definir bandera Como Logico
	
	flag = Verdadero
	Mientras flag = Verdadero hacer
		Escribir "Ingrese la edad del alumno (pulse 0 para terminar)"
		leer edad 
		Escribir "La edad es:  ", edad
		Si edad = 0 Entonces
			flag = Falso
		SiNo
			contadorAlumno = contadorAlumno + 1
			acuml_edad = acuml_edad + edad
		FinSi
	FinMientras
	
	promedio = acuml_edad / contadorAlumno
	Escribir "Los resultados son:"
	Escribir "Cantidad de alumnos ", contadorAlumno
	Escribir "Suma de edades ", acuml_edad
	Escribir "El promedio de edades es: ", promedio
	
FinAlgoritmo
	