from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    disponible: bool = True
    
# BBDD
productos_db: List[Producto] = [
    Producto(id=1, nombre="leche", precio=10, disponible=True),
    Producto(id=2, nombre="galleta", precio=20, disponible=False),
    Producto(id=3, nombre="choco", precio=40, disponible=True),
]

@app.get("/productos", response_model=List[Producto])
def listar_productos():
    return productos_db

@app.get("/productos/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int):
    for p in productos_db:
        if p.id == producto_id:
            return p