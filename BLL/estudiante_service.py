from DAL.estudiantes_repository import EstudianteRepository
from BLL.connection_manager import ConnectionManager

class EstudianteService():

    __connection_manager = ConnectionManager()
    __estudiante_repository = EstudianteRepository(__connection_manager.get_connection())


    def guardar_estudiante(self, estudiante):
        self.__connection_manager.open_connection()
        self.__estudiante_repository.guardar_estudiante(estudiante)
        self.__connection_manager.close_connection()
        return "El cliente ha sido registrado con éxito."

    def guardar_producto(self, producto):
        self.__connection_manager.open_connection()
        self.__estudiante_repository.guardar_producto(producto)
        self.__connection_manager.close_connection()
        return "El producto ha sido registrado con éxito."

    def obtener_todos(self):
        self.__connection_manager.open_connection()
        estudiante = self.__estudiante_repository.obtener_todos()
        self.__connection_manager.close_connection()
        return estudiante

    def obtener_cliente(self):
        self.__connection_manager.open_connection()
        estudiante = self.__estudiante_repository.obtener_cliente()
        self.__connection_manager.close_connection()
        return estudiante

    def obtener_producto(self):
        self.__connection_manager.open_connection()
        productos = self.__estudiante_repository.obtener_producto()
        self.__connection_manager.close_connection()
        return productos