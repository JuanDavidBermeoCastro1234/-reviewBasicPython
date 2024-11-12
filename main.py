# Ejercicio 5: Días de la semana
# Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la
# semana usando match .
# Enunciado:
# Solicita al usuario un número del 1 al 7 y muestra el día de la semana correspondiente (1 = Lunes,
# 7 = Domingo).
import math

days_of_the_week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

day=int(input("What day of the week do you want to see? Enter the number : "))

print(days_of_the_week [day-1])