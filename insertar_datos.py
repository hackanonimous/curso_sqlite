
# ingresaremos un cliente.
# ingresaremos 5 productos

import sqlite3
try:
    conn=sqlite3.connect("insert_data.db")
    print("-----CONEXION EXITOSA-----")
    cursor=conn.cursor()
    """
    recuerde que en esta seccion debera estar creado previamente las tablas en este caso cliente y producto.
    """
    #insertando un cliente
    #crear la query
    query_client="INSERT INTO cliente (nombre,apellido,celular,email) VALUES (?,?,?,?)"
    data_client=("jose","alvarez",917452076,"esi.segurity@gmail.com")
    #ejecutamos nuestra query con la data
    cursor.execute(query_client,data_client)
    #confirmamos el registro
    conn.commit()
    
    #insertando 5 productos
    #creamos la query
    query_products="INSERT INTO producto (nombre,cantidad,stock,precio,descripcion) VALUES (?,?,?,?,?)"
    #creamos la data en este caso al ser varios datos creamos una lista de tuplas
    data_products=[
        ("gaseosa",5,10,2.50,"hola"),
        ("chocolate",10,10,1.50,"soy choco"),
        ("ajinomen",5,20,2.00,"caldito"),
        ("yogurt",8,20,7.50,"de leche"),
        ("takis",7,500,4.00,"picantes")
    ]
    #ejecutamos la query y la data pero en este caso al ser varios registros usaremos exectuemany
    cursor.executemany(query_products,data_products)
    #confirmamos el registro en nuestra base de datos
    conn.commit()
except sqlite3.Error as e:
    print(e)
finally:
    if conn:
        conn.close()