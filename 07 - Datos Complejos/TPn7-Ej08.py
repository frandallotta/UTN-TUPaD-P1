productos = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 20
}

while True:
    print("\nOpciones:")
    print("1 - Consultar stock")
    print("2 - Agregar unidades a un producto existente")
    print("3 - Agregar un nuevo producto")
    print("4 - Salir")

    opcion = input("Ingrese una opción (1-4): ")

    if opcion == "1":
        producto = input("\nIngrese el nombre del producto a consultar: ")
        if producto in productos:
            print(f"Stock de {producto}: {productos[producto]} unidades")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")

    elif opcion == "2":
        producto = input("\nIngrese el nombre del producto: ")
        if producto in productos:
            cantidad = int(input(f"Ingrese la cantidad a agregar a {producto}: "))
            productos[producto] += cantidad
            print(f"Nuevo stock de {producto}: {productos[producto]} unidades")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")

    elif opcion == "3":
        producto = input("\nIngrese el nombre del nuevo producto: ")
        if producto in productos:
            print(f"El producto '{producto}' ya existe. Use la opción 2 para agregar stock.")
        else:
            cantidad = int(input(f"Ingrese la cantidad inicial de {producto}: "))
            productos[producto] = cantidad
            print(f"Producto '{producto}' agregado con {cantidad} unidades.")

    elif opcion == "4":
        print("\nSaliendo del programa...")
        break

    else:
        print("\nOpción no válida, intente nuevamente.")