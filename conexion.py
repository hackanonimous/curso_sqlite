#importamos el modulo sqlite3
import sqlite3

#instanciamos sqlite con el metodo connect el cual recibira como parametro el nombre del archivo de base de datos
conn=sqlite3.connect("my.db")
#conn sera el objeto Connection que retornara connect
#connect se conectara al archivo my.db y de no encontrar el archivo lo creara y generara la conexcion

#como buena practica debemos cerrar la conexion, para eso devemos usar el metodo close() de nuestro objeto Connection
conn.close()