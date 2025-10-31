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


print("\nProductos disponibles:")
for i in productos:
    print(f"{i['nombre']} - ${i['precio']} ({i['cantidad']} unidades)")


print("\nBuscar producto:")
buscado = input("Ingrese el nombre del producto a buscar: ")

encontrado = False

for i in productos:
    if i["nombre"].lower() == buscado.lower():
        print(f"\nProducto encontrado!")
        print(f"Nombre: {i['nombre']}")
        print(f"Precio: ${i['precio']}")
        print(f"Cantidad: {i['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nProducto no encontrado en la lista.")