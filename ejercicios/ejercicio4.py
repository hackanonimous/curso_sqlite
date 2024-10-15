# actualizar la tabla cliente tenemos 3 registros con los mismos datos tenemos 
# que actualizarlos con nueva infromacion
import sqlite3
try:
    #creamos un contexto
    #cuando salimos del contexto la conexcion se cerrar automaticamente
    #evitamos crear el finally y el conn.close()
    with sqlite3.connect("./ejercicios/databases/primera_conexion.db") as conn:
        cursor=conn.cursor()
        query="UPDATE cliente SET nombre=?,apellido=?,celular=?,email=? WHERE id=?;"
        #ejecutar la sentencia reemplazando el marcador posicional por los datos a actualizar
        cursor.execute(query,("guianluca","alvarez",9234567823,"milan@gmail.com",3))
        #confirmamos la percintencia de datos
        conn.commit()
except sqlite3.Error as e:
    print(e)