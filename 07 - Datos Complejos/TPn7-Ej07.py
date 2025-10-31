parcial1 = set()
parcial2 = set()

print("Ingrese los nombres de los estudiantes que aprobaron Parcial 1 (deje vacío para terminar):")
while True:
    nombre = input("Nombre: ").strip()
    if nombre == "":
        break
    parcial1.add(nombre)


print("\nIngrese los nombres de los estudiantes que aprobaron Parcial 2 (deje vacío para terminar):")
while True:
    nombre = input("Nombre: ").strip()
    if nombre == "":
        break
    parcial2.add(nombre)


ambos = parcial1 & parcial2
print("\nAprobó ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobó solo uno de los parciales:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobó al menos un parcial:", al_menos_uno)