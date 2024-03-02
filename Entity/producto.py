from pydantic import BaseModel

class Producto(BaseModel):  # class notas(BaseModel)
    id_cliente: int
    nombre_producto: str
    valor: float

class ProductoResponse(BaseModel):
    id_cliente: int
    nombre_producto: str = None
    valor: float
