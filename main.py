from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from database import engine, Base
from routes.alumnos import router as alumnos_router
from routes.login import router as login_router
from routes.profesor import router as profesor_router
from routes.asistencia_api import router as asistencia_router
from routes.generarExcel import router as generar_excel_router
from routes.horarioProfesor import router as horario_profesor_router
from routes.terminal_api import router as terminal_router
from routes.asistencia_profesor import router as asistencia_profesor_router
from pathlib import Path

app = FastAPI()

# Obtener la ruta absoluta a la carpeta "frontend"
BASE_DIR = Path(_file_).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://127.0.0.1:5501",
        "http://192.168.1.40:5500",
        "*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(alumnos_router, prefix="/api")
app.include_router(login_router)
app.include_router(profesor_router)
app.include_router(asistencia_router)
app.include_router(generar_excel_router)
app.include_router(horario_profesor_router)
app.include_router(terminal_router)
app.include_router(asistencia_profesor_router)

# Evento startup para crear tablas (opcional en desarrollo)
@app.on_event("startup")
async def startup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Ruta raíz
@app.get("/")
async def root():
    return {"message": "Sistema de Asistencia RFID"}

# Bloque para que funcione en Render o localmente
if _name_ == "_main_":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))  # Render define PORT, local usa 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port)