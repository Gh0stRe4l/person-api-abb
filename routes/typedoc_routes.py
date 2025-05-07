from fastapi import APIRouter
from pydantic import BaseModel

typedoc_router = APIRouter()

# Modelo de tipo de documento
class TypeDoc(BaseModel):
    code: str  # Código del tipo de documento
    description: str  # Descripción del tipo de documento

# Base de datos en memoria para los tipos de documentos
typedocs_db = []

# Ruta para obtener todos los tipos de documentos
@typedoc_router.get("/typedocs")
def get_typedocs():
    return typedocs_db  # Devolvemos la lista de tipos de documentos almacenados

# Ruta para agregar un tipo de documento
@typedoc_router.post("/typedocs/add")
def add_typedoc(typedoc: TypeDoc):
    typedocs_db.append(typedoc)  # Añadimos el nuevo tipo de documento a la base de datos
    return {"message": "TypeDoc added successfully", "typedoc": typedoc}
