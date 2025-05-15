from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

person_router = APIRouter()

class Person(BaseModel):
    name: str
    age: int
    document_type: str
    document_number: str
    father_id: Optional[str] = None
    mother_id: Optional[str] = None

persons_db = []

@person_router.get("/persons")
def get_persons():
    return persons_db

@person_router.post("/persons/add")
def add_person(person: Person):
    persons_db.append(person)
    return {"message": "Person added successfully", "person": person}

@person_router.get("/persons/{person_id}")
def get_person_by_id(person_id: str):
    for person in persons_db:
        if person.document_number == person_id:
            return person
    raise HTTPException(status_code=404, detail="Person not found")

@person_router.put("/persons/{person_id}")
def update_person(person_id: str, updated_person: Person):
    for index, person in enumerate(persons_db):
        if person.document_number == person_id:
            persons_db[index] = updated_person
            return {"message": "Person updated successfully", "person": updated_person}
    raise HTTPException(status_code=404, detail="Person not found")

@person_router.delete("/persons/{person_id}")
def delete_person(person_id: str):
    for index, person in enumerate(persons_db):
        if person.document_number == person_id:
            deleted = persons_db.pop(index)
            return {"message": "Person deleted successfully", "person": deleted}
    raise HTTPException(status_code=404, detail="Person not found")

@person_router.get("/persons/{person_id}/parents")
def get_person_parents(person_id: str):
    # Buscar a la persona
    target = None
    for person in persons_db:
        if person.document_number == person_id:
            target = person
            break
    if not target:
        raise HTTPException(status_code=404, detail="Person not found")

    # Buscar a los padres si existen
    father = next((p for p in persons_db if p.document_number == target.father_id), None)
    mother = next((p for p in persons_db if p.document_number == target.mother_id), None)

    return {
        "person": target,
        "father": father,
        "mother": mother
    }

@person_router.get("/persons/{person_id}/children")
def get_person_children(person_id: str):
    # Buscar hijos de esta persona como padre o madre
    children = [p for p in persons_db if p.father_id == person_id or p.mother_id == person_id]

    if not children:
        return {"message": "This person has no registered children."}

    return {
        "parent_id": person_id,
        "children": children
    }
