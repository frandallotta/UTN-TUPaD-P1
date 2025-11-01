def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("\nIngrese la posición hasta la que desea mostrar la serie de Fibonacci: "))

print("\nSerie de Fibonacci hasta la posición", posicion, ":")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")