# Ejercicio 16: Cálculo del tiempo de viaje
# Escribe un programa que calcule el tiempo que tarda en llegar un automóvil a su destino.
# Enunciado:
# Solicita al usuario la distancia a recorrer (en km) y la velocidad promedio del automóvil (en km/h).
# Calcula el tiempo de viaje en horas y minutos. Si la velocidad es mayor a 120 km/h, muestra un
# mensaje de advertencia.

# Input data
distance = float(input("Enter the distance in km: "))
speed = float(input("Enter the speed in km/h: "))

# Calculate the total time in hours
total_time_hours = distance / speed

# Get the hours (integer part)
hours = int(total_time_hours)

# Get the minutes (decimal part * 60)
minutes = round((total_time_hours - hours) * 60)

# Display the result
print(f"The travel time is {hours} hours and {minutes} minutes.")

if speed>120:
    print(F"BE CAREFUL ABOUT EXCESSIVE SPEEDING")
