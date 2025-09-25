cpar = 0
cimpar = 0
cpositivo = 0
cnegativo = 0
ccero = 0

for i in range (1,101):
    numero = int(input(f"Ingrese su numero nº{i} : "))

    if numero % 2 == 0:
        cpar = cpar + 1
    else:
        cimpar = cimpar + 1

    if numero>0:
        cpositivo = cpositivo + 1
    elif numero<0:
        cnegativo = cnegativo + 1
    else:
        ccero = ccero + 1

print ("Cantidad de numeros POSITIVOS:", cpositivo)
print ("Cantidad de numeros NEGATIVOS:", cnegativo)
print ("Cantidad de numeros PARES:", cpar)
print ("Cantidad de numeros IMPARES:", cimpar)
print ("Cantidad de numeros iguales a CERO:", ccero)