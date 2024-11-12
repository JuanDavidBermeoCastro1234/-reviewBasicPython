# Solicitar dos números y la operación a realizar
# Ejercicio 4: Determinación del tipo de triángulo
# Escribe un programa que determine el tipo de triángulo en función de sus lados usando if .
# Enunciado:
# Solicita al usuario que ingrese las longitudes de los tres lados de un triángulo. Determina si el
# triángulo es equilátero, isósceles o escaleno.
   
lado1=float(input(" Enter the first side of the triangle : "))
lado2=float(input(" Enter the second side of the triangle : "))
lado3=float(input(" Enter the third side of the triangle : "))

if lado1==lado2==lado3:
    print(f"the triangle is equilateral ")
elif lado1!= lado2!=lado3:
    print(f"the triangle is escaleno  ")
else:
    print("the triangle is isoceles ")