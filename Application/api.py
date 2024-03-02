from fastapi import APIRouter
import numpy
from BLL.connection_manager import ConnectionManager
from Entity.estudiante import Estudiante
from Entity.producto import Producto

from BLL.estudiante_service import EstudianteService

router = APIRouter()

estudiante_service = EstudianteService()
connection = ConnectionManager()


@router.post("/guardar_estudiante")
def guardar_estudiante(estudiante: Estudiante):
    return estudiante_service.guardar_estudiante(estudiante)

@router.post("/guardar_producto")
def guardar_producto(producto: Producto):
    return estudiante_service.guardar_producto(producto)

@router.get("/obtener_todos")
def obtener_todos():
    return estudiante_service.obtener_todos()

@router.get("/obtener_cliente")
def obtener_cliente():
    return estudiante_service.obtener_cliente()

@router.get("/obtener_producto")
def obtener_producto():
    return estudiante_service.obtener_producto()