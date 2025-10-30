def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
   
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

resultados = operaciones_basicas(num1, num2)


print("\nResultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")