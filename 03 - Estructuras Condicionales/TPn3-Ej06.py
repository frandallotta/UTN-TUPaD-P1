import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1,100) for i in range (50)]

media = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mean(numeros_aleatorios)

print("Lista de números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("La distribución tiene sesgo positivo")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
