def factorial(num):
    
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


n = int(input("Ingrese un número entero: "))

for i in range(1, n + 1):
    print(f"El factorial de {i} es {factorial(i)}")