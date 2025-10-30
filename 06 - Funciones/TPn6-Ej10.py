def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

resultado = calcular_promedio(a, b, c)
print(f"\nEl promedio de los tres números es: {resultado:.2f}")