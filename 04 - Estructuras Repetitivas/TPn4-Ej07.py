numero1 = -1
suma = 0

while numero1 < 0:
    numero1 = int(input("Ingrese un número entero positivo: "))
    if numero1 < 0:
        print("\nNumero inválido, intente de nuevo.\n")

for i in range (0, numero1 + 1):
    suma = suma + i

print("\nLa suma de los números desde 0 hasta", numero1, "es:", suma)