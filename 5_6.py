
def comparar_edades(e1, e2):
    if e1 > e2:
        return f"Hermano 1 es mayor por {e1-e2} años."
    elif e2 > e1:
        return f"Hermano 2 es mayor por {e2-e1} años."
    else:
        return "Ambos hermanos tienen la misma edad."

def main():
    e1 = int(input("Edad del hermano 1: ").strip())
    e2 = int(input("Edad del hermano 2: ").strip())
    print(comparar_edades(e1, e2))

if __name__ == '__main__':
    main()
