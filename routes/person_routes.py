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
    for person in persons_db:
        if person.document_number == person_id:
            return person
    raise HTTPException(status_code=404, detail="Person not found")

# Ruta para actualizar una persona
@person_router.put("/persons/{person_id}")
def update_person(person_id: str, updated_person: Person):
    for index, person in enumerate(persons_db):
        if person.document_number == person_id:
            persons_db[index] = updated_person
            return {"message": "Person updated successfully", "person": updated_person}
    raise HTTPException(status_code=404, detail="Person not found")

# 🗑 Ruta para eliminar una persona
@person_router.delete("/persons/{person_id}")
def delete_person(person_id: str):
    for index, person in enumerate(persons_db):
        if person.document_number == person_id:
            deleted = persons_db.pop(index)
            return {"message": "Person deleted successfully", "person": deleted}
    raise HTTPException(status_code=404, detail="Person not found")
