filas = int(input("Ingrese la cantidad de filas: "))

for i in range(1, filas + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # esto sí salta de línea, para pasar a la siguiente fila