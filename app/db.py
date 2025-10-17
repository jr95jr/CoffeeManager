from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ⚙️ Configuración de conexión a MySQL Workbench
USER = "root"
PASSWORD = "76377820"
HOST = "localhost"
PORT = "3306"
DB_NAME = "coffeemanager_db"

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# Crear motor y sesión
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para definir tablas
Base = declarative_base()
