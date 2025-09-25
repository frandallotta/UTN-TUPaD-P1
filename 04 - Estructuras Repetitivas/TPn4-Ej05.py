import random 
numero = random.randint(0, 9)
intentos = 0

while True:
    nadivinar = int(input("Adivine el numero aleatorio entre 0 & 9: "))
    
    if nadivinar == numero:
        break
    
    intentos = intentos + 1

print ("ADIVINASTE!! Cantidad de intentos:", intentos)