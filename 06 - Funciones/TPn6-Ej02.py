def saludar_usuario(nombre):
    return f"Hola {nombre}!"


nombre_ingresado = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_ingresado)
print(saludo)