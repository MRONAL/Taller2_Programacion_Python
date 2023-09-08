positivos = 0
negativos = 0

print("Ingrese valores enteros (0 para terminar):")

valor = 1  # Inicializamos valor con cualquier número diferente de 0 para entrar en el bucle

while valor != 0:
    valor = int(input())

    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

print("Gráfico de valores positivos y negativos:")
print("Positivos: " + "*" * positivos)
print("Negativos: " + "*" * negativos)