import sqlite3
try:
    conn=sqlite3.connect("relacion.db")
    cursor=conn.cursor()
    #creamos una variable que tendra en una lista las sentencias que debera excutar
    query=[
        """
        CREATE TABLE Proyectos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            fecha_inicio TEXT,
            fecha_termino TEXT
        );
        """,
        """
        CREATE TABLE Tareas(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            prioridad INT,
            proyecto_id INT NOT NULL,
            estado INT NOT NULL,
            fecha_inicio TEXT,
            fecha_termino TEXT,
            FOREIGN KEY (proyecto_id) REFERENCES Proyectos (id)
        );
        """
    ]
    #con un for recorremos y los ejecutamos
    for sentencia in query:
        cursor.execute(sentencia)
    conn.commit()
except sqlite3.Error as e:
    print(e)
finally:
    if conn:
        conn.close()