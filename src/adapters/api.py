from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.core.use_cases import UserService

app = FastAPI()
user_service = UserService()

class UserCreateRequest(BaseModel):
    name: str
    email: str
    password: str
    profile_picture: Optional[str] = None

@app.post("/users/", response_model=dict)
async def create_user(user: UserCreateRequest):
    created_user = user_service.create_user(user.name, user.email, user.password, user.profile_picture)
    return {"message": "User created successfully", "user": created_user}

@app.get("/users/", response_model=list)
async def get_users():
    return user_service.get_users()

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    if user_service.delete_user(user_id):
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
