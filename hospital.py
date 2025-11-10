from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Lista para almacenar los pacientes
pacientes_db = []

class Contacto(BaseModel):
    telefono: str
    email: Optional[str] = None
    
class Paciente(BaseModel):
    nombre: str
    apellido: str
    edad: int
    contacto: Contacto
    """
    alergias: Optional[str] = []
    activo: Optional[bool] = True
    """    
    
# registra un nuevo paciente
@app.post("/pacientes")
async def crear_paciente(paciente: Paciente):
    # Guardar el libro en la lista
    pacientes_db.append(paciente.model_dump())
    
    return {
        "mensaje": f"Se ha creado el paciente {paciente.nombre} con éxito",
        "datos": {
            "nombre": paciente.nombre,
            "apellido": paciente.apellido,
            "edad": paciente.edad,
            "contacto": paciente.contacto
            
        }
    }
    
    
            

# devuelve la lista de todos los pacientes
@app.get("/pacientes")
def ver_pacientes():
    return {
        "total": len(pacientes_db),
        "libros": pacientes_db
    }

"""

# devuelve un paciente especifico    
@app.get("/paciente/{paciente_id}")
def ver_libros():
    return {
        "total": len(pacientes_db),
        "libros": pacientes_db
    }

# devuelve solo pacientes activos
@app.get("/pacientes/activos")
def ver_libros():
    return {
        "total": len(pacientes_db),
        "libros": pacientes_db
    }
    
"""
"""
alergias": paciente.alergias,
"activo": paciente.activo 
"""    