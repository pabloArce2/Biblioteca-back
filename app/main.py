from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user as user_routes
from app.database import Base, engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por la URL de tu frontend en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (POST, GET, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

# Incluir las rutas de usuarios
app.include_router(user_routes.router, prefix="/users", tags=["users"])
