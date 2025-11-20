from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Boolean, String, Integer, Float

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int
    disponible: bool

# copiar hasta aqui para tu BBDD
# usar sqlite correctamente; './' crea el archivo en el directorio de trabajo
# La linea de abajo super importante la direccion para que se cargue sqlite
DATABASE_URL = "sqlite:///./productos_prueba_db.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
# autoflush impide una consulta sin confirmacion y autocommit que no se sube un valor nuevo en una tabla
SessionLocal = sessionmaker(
    autocommit=False,
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
#crear 3 objetos
db = SessionLocal()

try:
    productos_existentes = db.query(ProductoORM).first()
    if not productos_existentes:
        productos = [
            ProductoORM(id=1, nombre="leche", precio=1.98, stock=23, disponible=True),
            ProductoORM(id=2, nombre="yogur", precio=1.8, stock=3, disponible=True),
            ProductoORM(id=3, nombre="galletas", precio=3.38, stock=223, disponible=False),
        ]
        db.add_all(productos)
        db.commit()
finally:
    db.close()
    
"""
class CategoriaORM

class CarritoORM
"""