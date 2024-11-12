# Ejercicio 13: Comparación de tres números
# Escribe un programa que determine el mayor de tres números usando if .
# Enunciado:
# Solicita al usuario que ingrese tres números y determina cuál es el mayor.

number1=int(input("Enter a number : "))
number2=int(input("Enter a number : "))
number3=int(input("Enter a number : "))

if number1>number2 and number1>number3:
    print(f"{number1} is older")
elif number2>number1 and number2>number3:
    print(f"{number2} is older")    
elif number3>number1 and number3>number2:
    print(f"{number3} is older")
else :
    print("The three numbers are equal")