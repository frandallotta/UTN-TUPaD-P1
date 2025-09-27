ventas = [
    [5, 3, 2, 7, 4, 6, 3],
    [2, 8, 1, 3, 5, 7, 4],
    [6, 4, 7, 2, 8, 8, 5],
    [3, 6, 4, 5, 2, 9, 7]
]
print("")
for i in range(len(ventas)):
    print(ventas[i])

totales_productos = []
print("\nTotal vendido por cada producto:")
for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    totales_productos.append(total_producto)
    print(f"Producto {i+1}: {total_producto}")

mayor_ventas = 0
dia_mayor = 0

print("\nTotal ventas diarias:")
for j in range(7):
    total_dia=0
    for i in range(4):
        total_dia += ventas[i][j]
    print(f"Total del dia {j+1}: {total_dia}")
    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j

print(f"\nEl dia con mayores ventas fue el {dia_mayor+1}, con {mayor_ventas} ventas.")

mayor_producto = 0
indice_mayor = 0

for i in range(4):
    if totales_productos[i]> mayor_producto:
        mayor_producto = totales_productos[i]
        indice_mayor = i

print(f"El producto mas vendido fue el {indice_mayor+1}, con {mayor_producto} ventas en la semana\n")