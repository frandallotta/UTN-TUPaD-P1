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


print("\nLista de productos cargados:")
for i in productos:
    print(f"Producto: {i['nombre']} | Precio: ${i['precio']} | Cantidad: {i['cantidad']}")

print("")