def decimal_a_binario(decimal):
    # Caso especial
    if decimal == 0:
        return "0", [(0, 0, 0)]
    
    binario = ""
    pasos = []
    
    while decimal > 0:
        residuo = decimal % 2
        cociente = decimal // 2
        pasos.append((decimal, cociente, residuo))
        decimal = cociente
        binario = str(residuo) + binario
    
    return binario, pasos


# Programa principal
while True:
    try:
        numero = int(input("\nIngrese un número entero positivo: "))
        if numero < 0:
            print("⚠️ Debe ingresar un número positivo.")
            continue
        break
    except ValueError:
        print("⚠️ Entrada no válida. Intente de nuevo.")

binario, pasos = decimal_a_binario(numero)

print("\nCálculo paso a paso:\n")
print(f"{'Dividendo':>10} {'÷ 2':>5} {'Cociente':>10} {'Residuo':>10}")
print("-"*40)

for dividendo, cociente, residuo in pasos:
    print(f"{dividendo:>10} {'÷ 2':>5} {cociente:>10} {residuo:>10}")

print(f"\n✅ El número binario es: {binario}\n")

