# Ejercicio 12: Calculadora de IMC (Índice de Masa Corporal)
# Escribe un programa que calcule el IMC y determine el estado de peso.
# Enunciado:
# Solicita al usuario su peso (en kg) y su altura (en metros). Calcula el IMC y clasifícalo en bajo peso
# (<18.5), peso normal (18.5-24.9), sobrepeso (25-29.9), o obesidad (>=30).



weight=float(input("Please enter your weight :"))
height=float(input("Please enter your height : "))

imc=weight/height**2

if imc<18.5:
    print(f"underweight")
elif imc>18.5 and imc<24.9:
    print(f"low normal")
elif imc>25 and imc<29.9:
    print(f"overweight")
elif imc>30:
    print(f"obesity")