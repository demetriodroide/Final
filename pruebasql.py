from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Boolean, String, Integer, Float
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int
    disponible: bool

# copiar hasta aqui para tu BBDD
DATABASE_URL = "sqllite:///./productos_prueba_db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)
# autoflush impide una consulta sin confirmacion y autocommit que no se sube un valor nuevo en una tabla
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)
# copiar hasta aqui para tu BBDD

# base declarativa
class Base(DeclarativeBase):
    pass

#modelo ORM SQLalchemy ( tabla ) minusculas con nombre de la entidad + s ( productos ) relaciono el campo BASE con BASEMODEL
# si no pones que sea nullable por defecto es True, no hace falta decir que es false, no puedo no haber clave primaria
class ProductoORM(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, nullable=False)

# el bind le dice donde tiene que crear las tablas
Base.metadata.create_all(bind=engine)
#crear sesion
db = SessionLocal()

"""
class CategoriaORM

class CarritoORM
"""