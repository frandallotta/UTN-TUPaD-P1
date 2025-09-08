nombre = input("Ingrese su nombre: ")
print("Si quiere su nombre en mayúsculas, ingrese: 1")
print("Si quiere su nombre en minúsculas, ingrese: 2")
print("Si quiere su nombre con la primera letra mayúscula, ingrese: 3")
numero = input("Ingrese su numero: ")

if (numero == "1"):
    nombre_mayusculas = nombre.upper()
    print (nombre_mayusculas)

elif (numero == "2"):
    nombre_minusculas = nombre.lower()
    print (nombre_minusculas)

elif (numero == "3"):
    nombre_titulo = nombre.title()
    print (nombre_titulo)

else:
    print("Ingrese un numero valido")