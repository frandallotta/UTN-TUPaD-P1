contactos = {}

print("Carga de contactos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero


print("\nContactos cargados:")
print(contactos)


consulta = input("\nIngrese el nombre del contacto a consultar: ")

if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print(f"No se encontró el contacto {consulta}")