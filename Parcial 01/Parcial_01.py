titulos = []
ejemplares = []
longitud=0
prestamo_devolucion = 0

while True:
    print("\n MENÚ PRINCIPAL:")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título") 
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")

    opcion = input("\nIngrese una opción: ")

    if opcion == "1":
        
        longitud = input("Ingrese la cantidad inicial de titulos: ")

        if not longitud.isnumeric():
            print("El valor ingresado debe ser un numero")

        else:
            longitud = int(longitud)
            titulos = []

            for i in range(longitud):
                libro = input(f"Ingrese el titulo {i+1}: ")
                titulos.append(libro)

    elif opcion == "2":
        
        if not titulos:
            print("Primero debe cargar títulos y ejemplares.")

        else:
            ejemplares = []

            for i in range(len(titulos)):
                copias = input(f"Ingrese la cantidad de copias del titulo '{titulos[i]}': ")
                ejemplares.append(copias)
    
    elif opcion == "3":
        if not titulos:
            print("Primero debe cargar títulos y ejemplares.")
        else:
            print("\nCATÁLOGO:")
            for i in range(len(titulos)):
                print(f"- {titulos[i]}: {ejemplares[i]} ejemplares")

    elif opcion == "4":
        if not titulos:
            print("Primero debe cargar títulos y ejemplares.")
        else:
            buscar = input("Ingrese el título a consultar: ")
            if buscar in titulos:
                indice = titulos.index(buscar)
                print(f"'{buscar}' tiene {ejemplares[indice]} ejemplares disponibles.")
            else:
                print(f"El libro '{buscar}' no se encuentra en el catálogo.")

    elif opcion == "5":
        if not titulos:
            print("Primero debe cargar títulos y ejemplares.")
        else:
            print("\nLibros agotados:")
            agotados = False

            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"- {titulos[i]}")
                    agotados = True
                    
            if not agotados:
                print("No hay libros agotados.")

    elif opcion == "6":
        
        libro = input(f"Ingrese el titulo del libro que desea agregar: ")
        titulos.append(libro)

        copias = int(input(f"Ingrese la cantidad de copias del titulo agregado: "))
        ejemplares.append(copias)
       
        print(f"Se agregó '{libro}' con {copias} ejemplares al catálogo.")

    elif opcion == "7":
        buscar = input(f"Ingrese el titulo del libro que desea actualizar: ")

        if buscar in titulos:
            indice = titulos.index(buscar)

            prestamo_devolucion = input("Elija una opción (P - Prestamo, D - Devolución): ")
            
            if str(prestamo_devolucion).lower() == "p":
                if ejemplares[indice] > 0:
                    ejemplares[indice] -= 1
                    print(f"Se realizó el préstamo de '{buscar}'.")
                else:
                    print(f"No hay ejemplares disponibles de '{buscar}'.")

            elif str(prestamo_devolucion).lower() == "d":
                ejemplares[indice] += 1
                print(f"Se registró la devolución de '{buscar}'.")
            else:
                print("Opción inválida.")

        else:
            print(f"El libro '{buscar}' no se encuentra en el catálogo.")

    elif opcion == "8":
        print("Saliendo del menu")
        break