temperatura = [
    [10,20],
    [11,21],
    [12,22],
    [13,23],
    [14,24],
    [15,25],
    [16,26],
]

for i in range(len(temperatura)):
    print(temperatura[i])

minima = [fila[0] for fila in temperatura]
maxima = [fila[1] for fila in temperatura]

print("\nTemperaturas minimas: ",minima)
print("Temperaturas maximas: ",maxima)

promedio_minima = sum(minima)/len(minima)
promedio_maxima = sum(maxima)/len(maxima)

print("\nEl promedio de minima es: ",promedio_minima)
print("El promedio de maxima es: ",promedio_maxima)

amplitudes = [fila[1] - fila[0] for fila in temperatura]
dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1
print("El día con mayor amplitud es:", dia_mayor_amplitud)