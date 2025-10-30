def segundos_a_horas(segundos):
    horas = segundos / 3600  
    return horas


segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")