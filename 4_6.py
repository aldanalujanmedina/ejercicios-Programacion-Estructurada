
def ordenar(a, b):
    return (a, b) if a <= b else (b, a)

def main():
    a = float(input("Ingrese número a: ").strip())
    b = float(input("Ingrese número b: ").strip())
    menor, mayor = ordenar(a, b)
    print(f"Ordenados: {menor}, {mayor}")

if __name__ == '__main__':
    main()
