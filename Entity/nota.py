from pydantic import BaseModel
from datetime import date


class Producto(BaseModel):              # class notas(BaseModel)
    id_estudiante: int
    nombre: str
    valor: str


class ProductoResponse(BaseModel):
    id_estudiante: str = int
    nombre: str = None
    valor: str = None
