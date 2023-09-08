import random

randomNumber = random.randint(1, 100)
intento = 0
intentoRealizados = 0

print("Adivina el número")

while intento != randomNumber:
    intento = int(input("Ingresa tu intento: "))
    intentoRealizados += 1

    if intento < randomNumber:
        print("El número pensado es mayor.")
    elif intento > randomNumber:
        print("El número pensado es menor.")
    else:
        print(f"¡Felicidades! Has adivinado el número {randomNumber} en {intentoRealizados} intentos.")