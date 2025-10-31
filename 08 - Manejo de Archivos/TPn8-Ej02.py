with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
       
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")