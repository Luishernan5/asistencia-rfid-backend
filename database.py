from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
import os

# Conexión asíncrona para producción (usando tus credenciales)
DATABASE_URL = "mysql+asyncmy://origaska_origaska:K(0u9co4G0n)BT@mysql.origaska.com:3306/origaska-rfid?charset=utf8mb4"

engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True para ver logs
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()  # Base para modelos SQLAlchemy

# Dependency para FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session