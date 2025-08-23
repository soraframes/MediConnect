from pydantic import BaseModel
from datetime import time, date

class CitaResponse(BaseModel):
    tipo_cita: str
    fecha: date
    hora: time
    nombre : str
    apellido: str
    estado: str


    class Config:
        from_attributes = True

class CitaResponse2(BaseModel):
    tipo_cita: str
    fecha: date
    hora: time
    nombre : str
    apellido: str
    estado: str
    hospital: str

    class Config:
        from_attributes = True
