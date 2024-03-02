from datetime import date
from pydantic import BaseModel, field_validator
from typing import List
from numpy import mean

class Estudiante(BaseModel):

    nombre: str
    identificacion: str
    fechaNacimiento: date
    sexo: str

    @field_validator("nombre")
    def validar_nombre(cls, value):
        if value != "":

            return value
        raise ValueError("Debe ingresar un nombre!")


class EstudianteResponse(BaseModel):
    nombre: str = None
    identificacion: str = None
    fechaNacimiento: date
    sexo: str = None
