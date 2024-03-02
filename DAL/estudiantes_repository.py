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

        sql = ("INSERT INTO clientes(identificacion, nombre, sexo, fecha_nacimiento) "
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

        sql = ("INSERT INTO productos(id_cliente, nombre_producto, valor) "
               "VALUES(%s, %s, %s)")

        values = (
            producto.id_cliente,                  # estudiante.identificacion,
            producto.nombre_producto,                          # cliente.nombre
            producto.valor)                           # cliente.sexo
           # str(estudiante.fechaNacimiento))

        cursor.execute(sql, values)
        self.connection.commit()
        cursor.close()

    def obtener_todos(self):
        clientes = []
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT nombre, identificacion, sexo, fecha_nacimiento, nombre_producto, valor"
            " FROM clientes c "  
            " LEFT JOIN productos p " 
            " ON c.id = p.id_cliente " 
            " GROUP BY identificacion "
        )
        result = cursor.fetchall()

        for item in result:
            clientes.append((item))

        cursor.close()
        return clientes

    def obtener_cliente(self):
        clientes = []
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT c.nombre, c.sexo, c.identificacion, c.fecha_nacimiento, p.nombre_producto"
            " FROM clientes c"
            " JOIN productos p"
            " ON c.id = p.id_cliente"
            " WHERE c.identificacion = 5829"

        )
        result = cursor.fetchall()
        for item in result:
            clientes.append((item))

        cursor.close()
        return clientes

    def obtener_producto(self):
        productos = []
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT nombre_producto, valor"
            " FROM productos"
        )
        result = cursor.fetchall()
        for item in result:
            productos.append((item))

        cursor.close()
        return productos