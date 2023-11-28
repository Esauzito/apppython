import requests
import json
import pandas as pd
#Solicitudes HTTP de cada tabla
def exportar_a_excel(url, nombre_archivo):
    query = requests.get(url)
    if query.status_code == 200:
        data = query.json()
        df = pd.DataFrame(data)
        df.to_excel(nombre_archivo, index=False)
        print(f"Datos exportados exitosamente a {nombre_archivo}")
    else:
        print(f"Error en la solicitud a {url}. Código de estado: {query.status_code}")

# Lista de tuplas que contienen la URL y el nombre de archivo para cada recurso
recursos = [
    ("http://localhost:3001/ventas", "ventas.xlsx"),
    ("http://localhost:3001/usuarios", "usuarios.xlsx"),
    ("http://localhost:3001/roles", "roles.xlsx"),
    ("http://localhost:3001/productos", "productos.xlsx"),
    ("http://localhost:3001/brands", "marcas.xlsx"),
    ("http://localhost:3001/estados", "estados.xlsx"),
    ("http://localhost:3001/categorias", "categorias.xlsx")
]

# Exportar cada recurso a un archivo Excel
for recurso in recursos:
    exportar_a_excel(recurso[0], recurso[1])