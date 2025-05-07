from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

person_router = APIRouter()

# Modelo de persona temporal
class Person(BaseModel):
    name: str
    age: int
    document_type: str
    document_number: str

# Base de datos en memoria
persons_db = []

# Ruta para obtener todas las personas
@person_router.get("/persons")
def get_persons():
    return persons_db

# Ruta para agregar una persona
@person_router.post("/persons/add")
def add_person(person: Person):
    persons_db.append(person)
    return {"message": "Person added successfully", "person": person}

# Ruta para obtener una persona por su document_number
@person_router.get("/persons/{person_id}")
def get_person_by_id(person_id: str):
    # Buscamos la persona en la base de datos por el document_number
    for person in persons_db:
        if person.document_number == person_id:  # Compara el document_number con el person_id recibido
            return person  # Si lo encontramos, devolvemos la persona
    raise HTTPException(status_code=404, detail="Person not found")  # Si no la encontramos, lanzamos error
