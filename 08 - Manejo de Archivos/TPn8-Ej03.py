with open("productos.txt", "r") as archivo:
    print("\nProductos actuales:")
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


print("\nAgregar nuevo producto:")
nombre_nuevo = input("Ingrese el nombre del producto: ")
precio_nuevo = input("Ingrese el precio: ")
cantidad_nueva = input("Ingrese la cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n")

print("\nProducto agregado correctamente!")