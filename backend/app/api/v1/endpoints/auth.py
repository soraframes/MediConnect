from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioLogin, Token
from app.schemas.usuario import ForgotPasswordRequest, ResetPasswordRequest
from app.services.auth_service import register_user, login_user
from app.services.auth_service import enviar_correo_recuperacion, restablecer_contrasena

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register", response_model=Token)
def register(user_data: UsuarioCreate, db: Session = Depends(get_db)):
    access_token = register_user(user_data, db)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(credentials: UsuarioLogin, db: Session = Depends(get_db)):
    access_token = login_user(credentials, db)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/recuperar-contrasena")
def recuperar_contrasena(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    # Aquí podrías validar que el correo existe antes de enviar
    enviar_correo_recuperacion(request.correo, db)
    return {"msg": "Te hemos enviado un correo para recuperar tu contraseña."}

@router.post("/restablecer-contrasena/{token}")
def restablecer_contra(token: str, request: ResetPasswordRequest, db: Session = Depends(get_db)):
    return restablecer_contrasena(token, request.nueva_contrasena, db)