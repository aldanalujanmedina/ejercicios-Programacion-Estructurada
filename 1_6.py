
def aprobado(n1, n2, n3):
    if n1 > 4 and n2 > 4 and n3 > 4 and (n1+n2+n3)/3 >= 7:
        return True
    return False

def main():
    n1 = float(input("Ingrese nota 1: ").strip())
    n2 = float(input("Ingrese nota 2: ").strip())
    n3 = float(input("Ingrese nota 3: ").strip())
    if aprobado(n1, n2, n3):
        print("El alumno aprueba la cursada.")
    else:
        print("El alumno no aprueba la cursada.")

if __name__ == '__main__':
    main()
