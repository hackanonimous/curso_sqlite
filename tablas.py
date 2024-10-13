import sqlite3
conn=sqlite3.connect("my2.db")

#almacenando el metodo de cursor en una varible este metodo nos permitira interactuar con la base de datos
cursor=conn.cursor()


try:
    #execute se le envia como argumento una sentencia SQL
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Alumnos(
                       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       apellido TEXT NOT NULL
                   )
                   """)
except sqlite3.Error as e:
    #manejamos el error para mostrarlo por terminal
    print(e)
finally:
    #si es correcto la ejecucio del codigo anteriro erificamos que exista la instanci de la conexion y lo cerramos
    if conn:
        conn.close()
