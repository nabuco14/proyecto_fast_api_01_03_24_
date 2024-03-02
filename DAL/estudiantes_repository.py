from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from Entity.estudiante import Estudiante, EstudianteResponse
from Entity.producto import Producto, ProductoResponse
from BLL.connection_manager import ConnectionManager

class EstudianteRepository():
    def __init__(self, connection):
        self.connection = connection

    def guardar_estudiante(self, estudiante: Estudiante):   # guardar_estudiante

        id = None
        cursor = self.connection.cursor()

        sql = ("INSERT INTO cliente(identificacion, nombre, sexo, fecha_nacimiento) "
               "VALUES(%s, %s, %s, %s)")

        values = (
            estudiante.identificacion,                  # estudiante.identificacion,
            estudiante.nombre,                          # cliente.nombre
            estudiante.sexo,                            # cliente.sexo
            str(estudiante.fechaNacimiento))

        cursor.execute(sql, values)
        self.connection.commit()
        id_estudiante = cursor.lastrowid
        cursor.close()

    def guardar_producto(self, producto: Producto):   # guardar_estudiante
        cursor = self.connection.cursor()

        sql = ("INSERT INTO producto(id_cliente, nombre, valor) "
               "VALUES(%s, %s, %s)")

        values = (
            producto.id_cliente,                  # estudiante.identificacion,
            producto.nombre,                          # cliente.nombre
            producto.valor)                           # cliente.sexo
           # str(estudiante.fechaNacimiento))

        cursor.execute(sql, values)
        self.connection.commit()
        cursor.close()

    def obtener_todos(self):
        clientes = []
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT identificacion, sexo, fecha_nacimiento, valor"
            " FROM cliente c "  
            " LEFT JOIN producto p " 
            " ON c.id = p.id_cliente " 
            " GROUP BY identificacion "
        )
        result = cursor.fetchall()
        for item in result:
            clientes.append((item))

        cursor.close()
        return clientes