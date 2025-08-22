from pydantic import BaseModel
from datetime import date

class PacienteResponse(BaseModel):
    nombre: str
    apellido: str

    class Config:
        from_attributes = True


class HistorialResponse(BaseModel):
    fecha: date
    nombre_paciente: str
    apellido_paciente: str
    nombre_medico: str
    apellido_medico: str
    tipo_cita: str
    estado_cita: str
    ubicacion: str

    class Config:
        orm_mode = True