datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_duplicar = []

for i in datos:
    if i not in sin_duplicar:
        sin_duplicar.append(i)

print ("Lista Original", datos)
print ("\nLista sin Duplicados", sin_duplicar)