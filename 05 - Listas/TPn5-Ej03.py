import random
lista_random=[]
lista_par=[]
lista_impar=[]

for i in range (15):
    numero = random.randint(1,100)
    lista_random.append(numero)

    if numero %2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print("Lista Original",lista_random)

print("\nLista numeros Par",lista_par)
print("Cantidad numeros Par",len(lista_par))

print("\nLista numeros Impar",lista_impar)
print("Cantidad numeros Imar",len(lista_impar))
