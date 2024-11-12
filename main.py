# Ejercicio 15: Cálculo del salario neto
# Escribe un programa que calcule el salario neto de un empleado después de aplicar impuestos.
# Enunciado:
# Solicita al usuario su salario bruto y su país de residencia. Calcula el salario neto aplicando
# impuestos: el 20% para residentes de "País A", el 15% para "País B" y el 10% para "País C". Si el
# país no está en la lista, aplica un 25% de impuestos


salary = float(input("Enter your salary: "))
country_b = salary / 0.15
country_a = salary / 0.20
country_c = salary / 0.10
other_country = salary / 0.25

country = input("Enter your country (a, b, c): ").lower()

if country == "a":
    print(f"Your salary after tax is {country_a}")
elif country == "b":
    print(f"Your salary after tax is {country_b}")
elif country == "c":
    print(f"Your salary after tax is {country_c}")
else:
    print(f"Your salary after tax is {other_country}")
