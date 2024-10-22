# crear una base de datos con las siguientes consideraciones
# la base de datos debera estar en la carpeta databases
# una base de datos basica de una biblioteca
# las siguientes entidades: usuario, libro, 
# la relacion debera ser de uno a mucho un usuario podra prestarse muchos libros
import sqlite3
query_table=[
    """
    CREATE TABLE usuario(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        dni INT NOT NULL,
        celular INT NOT NULL,
        email TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE libro(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        estado_prestamo INT,
        usuario_id INT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuario(id)
    )
    """
]
query_usuario="""
    INSERT INTO usuario(nombre,dni,celular, email) VALUES (?,?,?,?)
"""
data_usuario=[
    ("jose",70133573,917452076,"esi.segurity@gmail.com"),
    ("adriano",74859632,987654321,"adriano@gmail.com")
]
query_libro="""
INSERT INTO libro(titulo,autor,estado_prestamo,usuario_id) VALUES(?,?,?,?)
"""
data_libro=[
    ("cien años de soledad","gabo",0,1),
    ("la ciudad y los perros","MVLL",1,2),
    ("ruinas circulares","borges",0,2),
    ("una cancion desesperada","mistral",1,1)
]
try:
    with sqlite3.connect("./ejercicios/databases/primera_conexion.db") as conn:
        cursor=conn.cursor()
        #creacion de las tablas
        for table in query_table:
            cursor.execute(table)
            conn.commit()
        #insercion de datos
        # dos usuario
        # cuatro libros
        cursor.executemany(query_usuario,data_usuario)
        conn.commit()
        cursor.executemany(query_libro,data_libro)
except sqlite3.Error as e:
    print(e)