print("Ingrese un número natural: ")
numero = int(input())

original = numero
inverso = 0

while numero > 0:
    digito = numero % 10
    inverso = inverso * 10 + digito
    numero //= 10

if original == inverso:
    print(original, "es un número palíndromo.")
else:
    print(original, "no es un número palíndromo.")