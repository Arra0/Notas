import streamlit as st
import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Crear una tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS datos (id INTEGER PRIMARY KEY, nombre TEXT)''')

# Widget para ingresar datos
nuevo_dato = st.text_input('Ingrese un nuevo dato:')

if st.button('Guardar'):
    if nuevo_dato:
        cursor.execute("INSERT INTO datos (nombre) VALUES (?)", (nuevo_dato,))
        conn.commit()

# Mostrar datos desde la base de datos
cursor.execute("SELECT * FROM datos")
datos = cursor.fetchall()
st.write("Datos almacenados:")
st.write(datos)

# Cerrar la conexión a la base de datos
conn.close()