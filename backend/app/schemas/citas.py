from pydantic import BaseModel
from datetime import time, date
from enum import Enum
from typing import Optional

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

#agendamiento de citas
class EstadoCita(str, Enum):
    PROGRAMADA = "Programada"
    CANCELADA = "Cancelada"
    COMPLETADA = "Completada"
    PENDIENTE = "Pendiente"


class CitaBase(BaseModel):
    id_paciente: int
    id_medico: int
    id_medicacion: int
    id_hospital: int
    id_info: int
    fecha: date
    hora: time
    id_info: Optional[int] = None
    estado: EstadoCita
    ubicacion: str


class CitaCreate(CitaBase):
    pass


class CitaResponseA(CitaBase):
    id_cita: int

    class Config:
        orm_mode = True


class CitaUpdate(BaseModel):
    id_paciente: int
    id_medico: int
    fecha: date
    hora: time
    tipo_cita: str
    estado: EstadoCita
    ubicacion: str