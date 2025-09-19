Algoritmo condicionales_ejercicio3
	definir harina, arroz, maicena, harina_p, arroz_p, maicena_p, harina_t, arroz_t, maicena_t, total Como Entero
	definir porcentaje Como Real
	
	Escribir "KG de harina: 20"
	Escribir "KG de arroz: 30"
	Escribir "KG de maicena: 25"
	Escribir "Ingrese cuantos kilos de cada producto desea comprar (en el mismo orden que la lista)"
	Leer harina, arroz, maicena 
	
	harina_p = 20
	arroz_p = 30
	maicena_p = 25
	
	harina_t = harina*harina_p 
	arroz_t = arroz*arroz_p
	maicena_t = maicena*maicena_p
	
	total = harina_t + arroz_t + maicena_t
	porcentaje = total - (10 * total) / 100
	
	Escribir "Los precios por producto son:"
	Escribir "Harina " harina_t
	Escribir "Arroz " arroz_t
	Escribir "Maicena " maicena_t
	Escribir "El precio total es: " total
	
	Si total > 100 Entonces
		Escribir "Tiene usted un 10% de descuento, por lo que su total final es de: " porcentaje
	FinSi
FinAlgoritmo
