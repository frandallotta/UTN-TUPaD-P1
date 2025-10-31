productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        
        nombre, precio, cantidad = linea.split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })


print("\nProductos actuales:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

opcion = input("\n¿Desea agregar un nuevo producto? (s/n): ").lower()

if opcion == "s":
    nombre_nuevo = input("Nombre del producto: ")
    precio_nuevo = float(input("Precio: "))
    cantidad_nueva = int(input("Cantidad: "))

    productos.append({
        "nombre": nombre_nuevo,
        "precio": precio_nuevo,
        "cantidad": cantidad_nueva
    })
    print("Producto agregado correctamente.")

buscado = input("\nIngrese el nombre de un producto a buscar: ")

encontrado = False
for p in productos:
    if p["nombre"].lower() == buscado.lower():
        print(f"\nProducto encontrado!")
        print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")


with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo 'productos.txt' actualizado correctamente!")