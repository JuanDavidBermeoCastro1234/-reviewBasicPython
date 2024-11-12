# Ejercicio 14: Adivinanza de letras
# Escribe un programa que permita al usuario adivinar una letra secreta usando match .
# Enunciado:
# El programa contiene una letra secreta (por ejemplo, "A"). El usuario debe adivinar la letra, y el
# programa le indicará si acertó o no.

value = input("Enter a value (A, B, C): ").lower()

if value == "a":
    print("You chose A")
elif value == "b":
    print("You chose B")
elif value == "c":
    print("You chose C")
else:
    print("Invalid value")