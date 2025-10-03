
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def main():
    anio = int(input("Ingrese un año: ").strip())
    if es_bisiesto(anio):
        print(f"El año {anio} es bisiesto.")
    else:
        print(f"El año {anio} NO es bisiesto.")

if __name__ == '__main__':
    main()
