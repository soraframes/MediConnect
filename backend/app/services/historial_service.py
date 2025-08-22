from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.planilla import VistaPlanilla  

def obtener_paciente(db: Session, id_paciente: int):
    paciente = (
        db.query(
            VistaPlanilla.nombre_paciente.label("nombre"),
            VistaPlanilla.apellido_paciente.label("apellido")
        )
        .filter(VistaPlanilla.id_paciente == id_paciente)
        .first()
    )

    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    return {"nombre": paciente.nombre, "apellido": paciente.apellido}



def obtener_historial(db: Session, id_paciente: int):
    historial = (
        db.query(
            VistaPlanilla.fecha,
            VistaPlanilla.nombre_paciente.label("nombre_paciente"),
            VistaPlanilla.apellido_paciente.label("apellido_paciente"),
            VistaPlanilla.nombre_medico.label("nombre_medico"),
            VistaPlanilla.apellido_medico.label("apellido_medico"),
            VistaPlanilla.tipo_cita.label("tipo_cita"),
            VistaPlanilla.estado_cita.label("estado_cita"),
            VistaPlanilla.ubicacion.label("ubicacion"),
        )
        .filter(VistaPlanilla.id_paciente == id_paciente)
        .all()
    )

    if not historial:
        raise HTTPException(status_code=404, detail="No se encontró historial clínico")

    return [
        {
            "fecha": h.fecha,
            "nombre_paciente": h.nombre_paciente,
            "apellido_paciente": h.apellido_paciente,
            "nombre_medico": h.nombre_medico,
            "apellido_medico": h.apellido_medico,
            "tipo_cita": h.tipo_cita,
            "estado_cita": h.estado_cita,
            "ubicacion": h.ubicacion,
        }
        for h in historial
    ]