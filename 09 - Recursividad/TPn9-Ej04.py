def decimal_a_binario(n):
    
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("\nIngrese un número entero positivo: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario}\n")