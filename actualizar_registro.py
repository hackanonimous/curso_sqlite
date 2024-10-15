# actualizar la tabla cliente tenemos 3 registros con los mismos datos tenemos 
# que actualizarlos con nueva infromacion
import sqlite3
try:
    #creamos un contexto
    #cuando salimos del contexto la conexcion se cerrar automaticamente
    #evitamos crear el finally y el conn.close()
    with sqlite3.connect("actualizar.db") as conn:
        cursor=conn.cursor()
        query="UPDATE cliente SET nombre=?,apellido=?,celular=?,email=? WHERE id=?;"
        #ejecutar la sentencia reemplazando el marcador posicional por los datos a actualizar
        cursor.execute(query,("guianluca","alvarez",9234567823,"milan@gmail.com",3))
        #confirmamos la percintencia de datos
        conn.commit()
        
    ### si deseamo actulizar con el mismo dato todos los registros de una columna en ese caso evitamos el where ejemplo:
        query2="UPDATE cliente SET email=?"
        #esta sentencia lograra que insertemos el mismo correo en todos los registros
        cursor.execute(query2,"admin@gmail.com")
        conn.commit()
except sqlite3.Error as e:
    print(e)