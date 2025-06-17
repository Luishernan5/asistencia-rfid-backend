import os

DB_USER = os.getenv('DB_USER', 'origaska_origaska')
DB_PASS = os.getenv('DB_PASSWORD', 'K(0u9co4G0n)BT')
DB_HOST = os.getenv('DB_HOST', '67.217.36.136')
DB_NAME = os.getenv('DB_NAME', 'origaska-rfid')

DATABASE_URL = f"mysql+asyncmy://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True para logs
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()

# Dependency para FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session