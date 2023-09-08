print("Piensa en un número entre 1 y 100.")
print("Cuando estés listo, ingresa < si es menor, > si es mayor o = si es correcto.")
input("Presiona enter para empezar")
minimo = 1
maximo = 100
adivinado = False

while not adivinado:
    intento = (minimo + maximo) // 2
    respuesta = input(f"¿Es {intento}? Ingresa <, > o =: ")

    if respuesta == "<":
        maximo = intento - 1
    elif respuesta == ">":
        minimo = intento + 1
    elif respuesta == "=":
        print(f"Es el numero: {intento} ¡Soy muy aspero xd!")
        adivinado = True
    else:
        print("Por favor, ingresa <, > o =.")