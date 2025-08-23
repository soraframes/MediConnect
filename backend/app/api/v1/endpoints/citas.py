
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.citas import CitaResponse, CitaResponse2
from app.services.citas_medicas import obtener_citas, obtener_cita
from typing import List

router = APIRouter(prefix="/Citas", tags=["Citas"])

@router.get("/Citas/{id_paciente}", response_model=List[CitaResponse])
def get_Usuarios(id_paciente: int, db: Session = Depends(get_db), ):
    return obtener_citas(db, id_paciente)

@router.get("/Cita/{id_cita}", response_model=CitaResponse2)
def get_paciente(id_cita: int, db: Session = Depends(get_db)):
    return obtener_cita(db, id_cita)


