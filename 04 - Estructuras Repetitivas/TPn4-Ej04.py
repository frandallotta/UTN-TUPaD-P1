suma = 0

while True:
    numero = int(input ("Ingrese un numero entero: (0 para terminar) \n"))

    if numero == 0:
        break

    suma = suma + numero
    
print ("La sumatoria de numeros es: ",suma )