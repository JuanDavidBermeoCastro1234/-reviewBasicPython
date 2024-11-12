# Ejercicio 7: Número positivo, negativo o cero
# Escribe un programa que determine si un número es positivo, negativo o cero usando if .
# Enunciado:
# Solicita al usuario que ingrese un número y determina si es positivo, negativo o cero.

number=float(input("Enter a number : "))

if number<0:
    print(f"number is negative ")
elif number>0:
    print(f"number is positive")
elif number==0:
    print(f"number equals zero") 