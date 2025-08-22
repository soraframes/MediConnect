# app/routes/historial.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.historial import PacienteResponse, HistorialResponse
from app.services import historial_service
from typing import List

router = APIRouter(prefix="/historial", tags=["Historial"])

@router.get("/paciente/{id_paciente}", response_model=PacienteResponse)
def get_paciente(id_paciente: int, db: Session = Depends(get_db)):
    return historial_service.obtener_paciente(db, id_paciente)


@router.get("/{id_paciente}", response_model=List[HistorialResponse])
def get_historial(id_paciente: int, db: Session = Depends(get_db)):
    return historial_service.obtener_historial(db, id_paciente)
