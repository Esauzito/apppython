import pandas as pd
import json
import requests

#Ingreso total de las ventas
consulta = requests.get('http://localhost:3001/ventas')
if consulta.status_code == 200:
    ventas = consulta.json()

    ingreso_total = 0

    for venta in ventas:
        cantidad = venta['cantidad']
        precio = float(venta['precio'])
        ingreso_total += cantidad * precio

    print(f'Ingreso Total: ${ingreso_total}')

else:
    print(f'Error al obtener datos de la API. Código de estado: {consulta.status_code}')
#Producto más vendido

# Hacer la solicitud a la API y obtener la respuesta en formato JSON
url = "http://localhost:3001/ventas"  # Reemplaza esto con la URL real de tu API
response = requests.get(url)
data = response.json()

# Crear un diccionario para almacenar las cantidades vendidas por producto
cantidades_por_producto = {}

# Iterar sobre los datos y sumar las cantidades por producto
for venta in data:
    producto = venta["producto"]
    cantidad = venta["cantidad"]

    if producto in cantidades_por_producto:
        cantidades_por_producto[producto] += cantidad
    else:
        cantidades_por_producto[producto] = cantidad

# Encontrar el producto más vendido
producto_mas_vendido = max(cantidades_por_producto, key=cantidades_por_producto.get)
cantidad_mas_vendida = cantidades_por_producto[producto_mas_vendido]

# Imprimir el resultado
print(f"El producto más vendido es '{producto_mas_vendido}' con {cantidad_mas_vendida} unidades vendidas.")
##Usuario que más ha gastado
url_ventas = "http://localhost:3001/ventas"
response_ventas = requests.get(url_ventas)
data_ventas = response_ventas.json()

usuarios_gasto = {}

for venta in data_ventas:
    usuario = venta["usuario"]
    cantidad = venta["cantidad"]
    precio = float(venta["precio"])

    gasto_total = cantidad * precio

    if usuario in usuarios_gasto:
        usuarios_gasto[usuario]["total_gasto"] += gasto_total
    else:
        usuarios_gasto[usuario] = {"total_gasto": gasto_total}

if usuarios_gasto:
    usuario_max_gasto = max(usuarios_gasto, key=lambda x: usuarios_gasto[x]["total_gasto"])
    gasto_maximo = usuarios_gasto[usuario_max_gasto]["total_gasto"]

    print(f"El usuario que ha gastado más es '{usuario_max_gasto}' con un gasto total de ${gasto_maximo:.2f}")
else:
    print("No hay datos de ventas en la API.")
#Promedio de gasto por usuario
url_ventas = "http://localhost:3001/ventas"
response_ventas = requests.get(url_ventas)
data_ventas = response_ventas.json()

usuarios_gasto = {}

for venta in data_ventas:
    usuario = venta["usuario"]
    cantidad = venta["cantidad"]
    precio = float(venta["precio"])

    gasto_total = cantidad * precio

    if usuario in usuarios_gasto:
        usuarios_gasto[usuario]["total_gasto"] += gasto_total
        usuarios_gasto[usuario]["total_ventas"] += 1
    else:
        usuarios_gasto[usuario] = {"total_gasto": gasto_total, "total_ventas": 1}

if usuarios_gasto:
    print("Promedio de gasto por usuario:")
    for usuario, datos in usuarios_gasto.items():
        promedio = datos["total_gasto"] / datos["total_ventas"]
        print(f"- {usuario}: ${promedio:.2f} por venta")
else:
    print("No hay datos de ventas en la API.")
#Productos que compra un usuario en promedio
url_ventas = "http://localhost:3001/ventas"
response_ventas = requests.get(url_ventas)
data_ventas = response_ventas.json()

usuarios_compras = {}

for venta in data_ventas:
    usuario = venta["usuario"]
    cantidad = venta["cantidad"]

    if usuario in usuarios_compras:
        usuarios_compras[usuario]["total_cantidad"] += cantidad
        usuarios_compras[usuario]["total_ventas"] += 1
    else:
        usuarios_compras[usuario] = {"total_cantidad": cantidad, "total_ventas": 1}

if usuarios_compras:
    print("Promedio de productos comprados por usuario:")
    for usuario, datos in usuarios_compras.items():
        promedio = datos["total_cantidad"] / datos["total_ventas"]
        print(f"- {usuario}: {promedio:.2f} productos por venta")
else:
    print("No hay datos de ventas en la API.")
#Productos actualmente en stock
url_productos = "http://localhost:3001/productos"
response_productos = requests.get(url_productos)
data_productos = response_productos.json()

productos_en_stock = []

for producto in data_productos:
    cantidad = int(producto["cantidad"])

    if cantidad > 0:
        productos_en_stock.append(producto)

if productos_en_stock:
    print("Productos actualmente en stock:")
    for producto in productos_en_stock:
        print(f"- {producto['producto']} (Cantidad actual: {producto['cantidad']})")
else:
    print("No hay productos en stock en este momento.")
#Productos con menos stock
url_productos = "http://localhost:3001/productos"
response_productos = requests.get(url_productos)
data_productos = response_productos.json()

productos_poco_stock = []

for producto in data_productos:
    cantidad = int(producto["cantidad"])

    if cantidad < 30:
        productos_poco_stock.append(producto)

if productos_poco_stock:
    print("Productos con menos de 30 unidades en stock:")
    for producto in productos_poco_stock:
        print(f"- {producto['producto']} (Cantidad actual: {producto['cantidad']})")
else:
    print("Todos los productos tienen suficiente stock.")
#Productos que necesitan ser reabastecidos
url_productos = "http://localhost:3001/productos"
response_productos = requests.get(url_productos)
data_productos = response_productos.json()

productos_para_reabastecer = []

for producto in data_productos:
    cantidad = int(producto["cantidad"])

    if cantidad < 10:
        productos_para_reabastecer.append(producto)

if productos_para_reabastecer:
    print("Productos que necesitan ser reabastecidos:")
    for producto in productos_para_reabastecer:
        print(f"- {producto['producto']} (Cantidad actual: {producto['cantidad']})")
else:
    print("Todos los productos tienen suficiente stock.")
#Producto más caro
url_productos = "http://localhost:3001/productos"
response_productos = requests.get(url_productos)
data_productos = response_productos.json()

producto_mas_caro = None
precio_mas_caro = float('-inf')

for producto in data_productos:
    precio = float(producto["precio"])

    if precio > precio_mas_caro:
        precio_mas_caro = precio
        producto_mas_caro = producto

if producto_mas_caro is not None:
    print(f"El producto más caro es '{producto_mas_caro['producto']}' con un precio de {precio_mas_caro:.2f}")
else:
    print("No hay datos de precios válidos en la API de productos.")
#Producto más barato
response_productos = requests.get(url_productos)
data_productos = response_productos.json()

producto_mas_barato = None
precio_mas_barato = float('inf')

for producto in data_productos:
    precio = float(producto["precio"])

    if precio < precio_mas_barato:
        precio_mas_barato = precio
        producto_mas_barato = producto

if producto_mas_barato is not None:
    print(f"El producto más barato es '{producto_mas_barato['producto']}' con un precio de {precio_mas_barato:.2f}")
else:
    print("No hay datos de precios válidos en la API de productos.")