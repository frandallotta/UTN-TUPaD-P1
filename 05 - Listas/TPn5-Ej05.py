alumnos = ["franco", "sofia", "martina", "lucas", "maximo", "cintia", "mauricio", "valentina"]

print (alumnos)

pregunta = int(input("\nIngrese 1 para agregar alguien a la lista: \nIngrese 0 para eliminar a alguien de la lista: \n"))

if pregunta == 1:
    nombre_agregar = input("\nIngrese el nombre que quiere agregar a la lista: ")
    alumnos.append(nombre_agregar)
    print(f"\nel alumno {nombre_agregar} fue agregado a la lista")

else:
    nombre_borrar = input("\nIngrese el nombre que quiere borrrar de la lista: ")
    
    if nombre_borrar in alumnos:
        alumnos.remove(nombre_borrar)
        print(f"\nel alumno {nombre_borrar} fue eliminado de la lista")
    else:
        print(f"\nel alumno {nombre_borrar} no existe en la lista")


print("Lista Modificada:",alumnos)