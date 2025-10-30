def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = float(input("Ingrese la temperatura en grados Celsius: "))

resultado = celsius_a_fahrenheit(celsius)
print(f"La temperatura equivalente en Fahrenheit es: {resultado:.2f}°F")