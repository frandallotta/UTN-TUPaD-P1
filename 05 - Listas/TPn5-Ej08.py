notas = [
    [7, 8, 6], 
    [5, 9, 7],  
    [9, 6, 4],  
    [4, 2, 9],   
    [1, 5, 3]   
]

for i in range(len(notas)):
    print(notas[i])

print("\nPromedio de cada estudiante:\n")
for i in range(5):
    suma=0
    for j in range(3):
        suma += notas [i][j]
    promedio = suma / 3
    print(f"Estudiante {i+1}: {promedio}")

print("\nPromedio de cada Materia:\n")
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas [i][j]
    promedio = suma / 5
    print(f"Promedio materia {j+1}: {promedio}")
    