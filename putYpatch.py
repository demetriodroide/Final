from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define aquí tus modelos Pydantic
class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoPatch(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None
    
# Define aquí tu lista de productos inicial
productos_db = [
    
    {"id":1, "nombre": "leche", "precio":10, "stock":3},
    {"id":2, "nombre": "queso", "precio":34, "stock":12},
    
]


# get para comprobaciones
@app.get("/productos")
def ver_productos():
    return productos_db


# Implementa aquí el endpoint PUT
@app.put("/productos/{producto_id}")
def actualizar_producto_entero(producto_id: int, producto: ProductoPatch):
    for i, valor in enumerate(productos_db):
        if valor["id"] == producto_id:
            
            productos_db[i] = {
                
                "id": producto_id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock
                
            }
            
            
            return productos_db[i]
    raise HTTPException(status_code=404, detail="404 producto no encontrado")

# Implementa aquí el endpoint PATCH
