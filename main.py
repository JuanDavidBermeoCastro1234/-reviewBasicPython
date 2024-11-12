# Ejercicio 8: Determinación de año bisiesto
# Escribe un programa que determine si un año es bisiesto o no.
# Enunciado:
# Solicita al usuario que ingrese un año y determina si es bisiesto (divisible entre 4, pero no entre
# 100, salvo que sea divisible entre 400).

year=int(input("enter a year please : "))

if year%4==0 and year!=0:
    print(F"is year bleap year ")
elif year%400==0:
    print(f"is year bleap year")
else:
    print(f"non leap year ")