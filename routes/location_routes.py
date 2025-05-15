# routes/location_routes.py

from fastapi import APIRouter, UploadFile, HTTPException
from models.models import Location  # Importación relativa corregida
from io import StringIO
import csv

location_router = APIRouter()

locations_db = []


@location_router.post("/upload")
def upload_csv(file: UploadFile):
    try:
        content = file.file.read().decode("utf-8")
        reader = csv.DictReader(StringIO(content))

        for row in reader:
            code = row.get("Código Municipio", "").strip()[:5]
            name = row.get("Nombre Municipio", "").strip().upper()
            state = row.get("Nombre Departamento", "").strip().upper()
            tipo = row.get("Tipo Centro Poblado", "").strip().lower()
            is_capital = tipo == "cabecera municipal"

            location_data = {
                "code": code,
                "name": name,
                "state": state,
                "is_capital": is_capital
            }

            locations_db.append(Location(**location_data))

        return {"status": "Locations loaded"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar el archivo: {str(e)}")


@location_router.get("/states")
def get_states():
    return list(set([loc.state for loc in locations_db]))


@location_router.get("/by-state/{state_code}")
def by_state(state_code: str):
    return [loc for loc in locations_db if loc.state == state_code]


@location_router.get("/by-code/{code}")
def by_code(code: str):
    for loc in locations_db:
        if loc.code == code:
            return loc
    raise HTTPException(status_code=404, detail="Location not found")


@location_router.get("/capitals")
def get_capitals():
    return [loc for loc in locations_db if loc.is_capital]
