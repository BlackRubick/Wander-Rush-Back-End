from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    profile_picture: Optional[str] = Field(default=None)  # URL o ruta de la foto de perfil
