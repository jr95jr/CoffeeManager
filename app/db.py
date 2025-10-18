from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ⚙️ Base declarativa
Base = declarative_base()

# 📦 Usar SQLite en lugar de MySQL
engine = create_engine("sqlite:///coffee_manager.db", connect_args={"check_same_thread": False})

Session = sessionmaker(bind=engine)
