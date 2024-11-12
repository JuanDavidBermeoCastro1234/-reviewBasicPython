# Ejercicio 6: Juego de adivinanza de números
# Escribe un programa que implemente un juego de adivinanza de números.
# Enunciado:
# El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número, y el
# programa indica si el número ingresado es mayor, menor o igual al número generado

import random

# Generar un número aleatorio entre 1 y 100 (Este es el número que solo tú sabrás)
random_number = random.randint(1, 100)

# Imprimir el número para que solo tú lo veas
#print(f"(El número aleatorio generado para adivinar es: {random_number})")

# Pedir un número al usuario
number = int(input("Ingresa un número entero, por favor: "))

# Mientras el número ingresado no sea el correcto, seguir pidiendo
while random_number != number:
    print("No has adivinado el número, sigue intentando.")
    number = int(input("Intenta con otro número: "))

# Si el número es correcto
print(f"¡Felicidades! Has adivinado el número.")