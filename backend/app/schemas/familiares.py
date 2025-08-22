from pydantic import BaseModel, EmailStr

class FamiliarBase(BaseModel):
    nombre: str
    correo: EmailStr
    id_info: int  

class FamiliarCreate(FamiliarBase):
    pass

class FamiliarResponse(FamiliarBase):
    id_familiar: int  # el ID autogenerado en la tabla
    class Config:
        from_attributes = True