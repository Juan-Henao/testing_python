from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Datos simulados
users_db = [
    {"id": 1, "name": "John Doe", "email": "johndoe@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "janedoe@example.com"}
]

# Modelo de datos
class User(BaseModel):
    id: int
    name: str
    email: str

# Obtener todos los usuarios
@app.get("/users/", response_model=List[User])
def get_users():
    return users_db

@app.get("/user/", response_model=User)
def get_users():
    return users_db[0]

# Crear un nuevo usuario
@app.post("/users/", response_model=User)
def create_user(user: User):
    if any(u["email"] == user.email for u in users_db):
        raise HTTPException(status_code=400, detail="Email already registered")
    users_db.append(user.dict())
    return user

# Eliminar un usuario por ID
@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    users_db.remove(user)
    return user

