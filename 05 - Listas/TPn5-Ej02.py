lista_productos = []

for i in range (5):
    producto = input(f"Ingrese el producto nº {i+1}: " )
    lista_productos.append(producto)

print ("\nLista de productos ingresada por el cliente:")
print (lista_productos)

print("\nLista de productos ordenada alfabeticamente:")
print(sorted(lista_productos))

borrar = input("\n¿Que elemento de la lista desea eliminar?: ")

if borrar in lista_productos:
    lista_productos.remove(borrar)
    print(f"\nel producto {borrar} fue eliminado de la lista")
else:
    print(f"\nel producto {borrar} no existe en la lista")

print("\nLista actualizada: ",lista_productos)