# conectarse a la base de datos que se encuentra en la carpeta databases y crear las siguientes tablas
## TABLAS
# producto - id, nombre, cantidad, stock, precio, descripcion
# cliente - id, dni, nombre, apellido, celular, email
# venta - id, producto_id, cliente_id 
## RELACIONES
# venta 1->m cliente
# venta 1->m prodcuto
import sqlite3
conn=sqlite3.connect("./ejercicios/databases/primera_conexion.db")
try:
    cursor=conn.cursor()
    querys=["""
           CREATE TABLE producto(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               cantidad INT NOT NULL,
               stock INT NOT NULL,
               precio REAL NOT NULL,
               descripcion TEXT
           );
           """,
           """
           CREATE TABLE cliente(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               apellido TEXT NOT NULL,
               celular INT NOT NULL,
               email TEXT NOT NULL
           );
           """,
           """
           CREATE TABLE venta(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               producto_id INT NOT NULL,
               cliente_id INT NOT NULL,
               FOREIGN KEY (producto_id) REFERENCES producto (id),
               FOREIGN KEY (cliente_id) REFERENCES cliente (id)
           );
           """]
    for query in querys:
        cursor.execute(query)
    conn.commit()    
except sqlite3.Error as e:
    print(e)
finally:
    if conn:
        conn.close()
