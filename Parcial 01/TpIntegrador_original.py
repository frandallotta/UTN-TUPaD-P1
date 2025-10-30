decimal = int(input("\nIngrese un numero entero: "))
print()

binario = ""
while (decimal>0):
    residuo = decimal%2
    cociente = decimal//2
    
    print(f"{decimal} ÷ 2 = {cociente}    Residuo = {residuo}")
    
    decimal = cociente
    binario = str(residuo) + binario
    
print(f"\nEl numero binario es: {binario}\n")