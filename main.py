# Ejercicio 11: Conversión de temperaturas
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Ask the user for temperature and scale
temperature = float(input("Enter a temperature: "))
scale = input("Enter a scale (C for Celsius, F for Fahrenheit): ").lower()

# Use match to perform the conversion
match scale:
    case "f":
        # Convert from Celsius to Fahrenheit
        fahrenheit_value = celsius_to_fahrenheit(temperature)
        print(f"The temperature {temperature}°C is equal to {fahrenheit_value}°F")
    case "c":
        # Convert from Fahrenheit to Celsius
        celsius_value = fahrenheit_to_celsius(temperature)
        print(f"The temperature {temperature}°F is equal to {celsius_value}°C")
    case _:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")