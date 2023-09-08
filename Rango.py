print("Ingrese la cantidad de datos: ")

cantidadDatos = int(input())
if cantidadDatos <= 0:
    print("La cantidad de datos debe ser mayor que cero.")
else:
    datos = [0] * cantidadDatos

    for i in range(cantidadDatos):
        print(f"Ingrese el dato #{i + 1}: ", end="")
        datos[i] = float(input())

    maximo = datos[0]
    minimo = datos[0]

    for i in range(1, cantidadDatos):
        if datos[i] > maximo:
            maximo = datos[i]
        if datos[i] < minimo:
            minimo = datos[i]

    rango = maximo - minimo

    print("El rango de los datos es:", rango)