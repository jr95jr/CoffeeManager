from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión a la base de datos MySQL que ya creaste
USER = "root"
PASSWORD = "76377820"
HOST = "localhost"
PORT = "3306"
DB_NAME = "coffee_manager"

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
