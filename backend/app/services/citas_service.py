from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.cita import Cita
from app.schemas.citas import CitaCreate, CitaUpdate

def crear_cita(db: Session, cita_data: CitaCreate):
    # Validar que el paciente no tenga cita a la misma fecha y hora
    cita_existente = db.query(Cita).filter(
        Cita.id_paciente == cita_data.id_paciente,
        Cita.fecha == cita_data.fecha,
        Cita.hora == cita_data.hora,
        Cita.estado != "CANCELADA"  #permitir que reagenden canceladas
    ).first()

    if cita_existente:
        raise HTTPException(
            status_code=400,
            detail="El paciente ya tiene una cita en esa fecha y hora"
        )

    # Validar que el médico no tenga otra cita a la misma fecha y hora
    medico_ocupado = db.query(Cita).filter(
        Cita.id_medico == cita_data.id_medico,
        Cita.fecha == cita_data.fecha,
        Cita.hora == cita_data.hora,
        Cita.estado != "CANCELADA"
    ).first()

    if medico_ocupado:
        raise HTTPException(
            status_code=400,
            detail="El médico ya tiene una cita en esa fecha y hora"
        )

    # Crear nueva cita
    nueva_cita = Cita(
        id_paciente=cita_data.id_paciente,
        id_medico=cita_data.id_medico,
        id_medicacion=cita_data.id_medicacion,
        id_hospital=cita_data.id_hospital,
        id_info=cita_data.id_info,
        fecha=cita_data.fecha,
        hora=cita_data.hora,
        tipo_cita=cita_data.tipo_cita,
        estado=cita_data.estado,
        ubicacion=cita_data.ubicacion
    )
    db.add(nueva_cita)
    db.commit()
    db.refresh(nueva_cita)
    return nueva_cita


def editar_cita(db: Session, cita_id: int, cita: CitaUpdate):
    db_cita = db.query(Cita).filter(Cita.id_cita == cita_id).first()
    if not db_cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")

    # Verificar que el paciente no tenga otra cita en la misma fecha y hora
    cita_existente_paciente = (
        db.query(Cita)
        .filter(
            Cita.id_paciente == cita.id_paciente,
            Cita.fecha == cita.fecha,
            Cita.hora == cita.hora,
            Cita.id_cita != cita_id  # excluye la misma cita
        )
        .first()
    )
    if cita_existente_paciente:
        raise HTTPException(status_code=400, detail="El paciente ya tiene una cita en esa fecha y hora")

    # Verificar que el médico no tenga otra cita en la misma fecha y hora
    cita_existente_medico = (
        db.query(Cita)
        .filter(
            Cita.id_medico == cita.id_medico,
            Cita.fecha == cita.fecha,
            Cita.hora == cita.hora,
            Cita.id_cita != cita_id
        )
        .first()
    )
    if cita_existente_medico:
        raise HTTPException(status_code=400, detail="El médico ya tiene una cita en esa fecha y hora")

    # Actualizar datos
    db_cita.id_paciente = cita.id_paciente
    db_cita.id_medico = cita.id_medico
    db_cita.fecha = cita.fecha
    db_cita.hora = cita.hora
    db_cita.tipo_cita = cita.tipo_cita
    db_cita.estado = cita.estado
    db_cita.ubicacion = cita.ubicacion

    db.commit()
    db.refresh(db_cita)
    return db_cita