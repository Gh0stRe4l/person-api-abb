from fastapi import FastAPI
from routes.person_routes import person_router
from routes.location_routes import location_router
from routes.typedoc_routes import typedoc_router

app = FastAPI()

# Registramos los routers para que las rutas sean accesibles
app.include_router(person_router)  # Rutas relacionadas con personas
app.include_router(location_router, prefix="/locations")  # Rutas relacionadas con ubicaciones, prefijo "/locations"
app.include_router(typedoc_router)  # Rutas relacionadas con tipo de documentos
