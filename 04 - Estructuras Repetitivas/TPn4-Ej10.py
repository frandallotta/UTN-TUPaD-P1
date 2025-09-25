numero=(input("Introduce el numero: "))

ndigitos = len(numero.lstrip("-"))

if ndigitos>=2:
    numeroinvertido=str(numero)[::-1]
    print(numeroinvertido)
else:
    print(numero)