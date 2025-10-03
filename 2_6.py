
def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    a = float(input("Ingrese lado 1: ").strip())
    b = float(input("Ingrese lado 2: ").strip())
    c = float(input("Ingrese lado 3: ").strip())
    print(f"El triángulo es {tipo_triangulo(a, b, c)}")

if __name__ == '__main__':
    main()
