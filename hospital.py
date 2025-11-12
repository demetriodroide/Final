from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Lista para almacenar los pacientes
pacientes_db = []

contador_id = 0

class Contacto(BaseModel):
    telefono: str
    email: Optional[str] = None
    
class Paciente(BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int
    contacto: Contacto
    alergias: Optional[str] = []
    activo: Optional[bool] = True
       
    
# registra un nuevo paciente
@app.post("/pacientes")
async def crear_paciente(paciente: Paciente):
    # Guardar el libro en la lista
    global contador_id
    contador_id += 1 
    pacientes_db.append(paciente.model_dump())
    
    return {
        "mensaje": f"Se ha creado el paciente {paciente.nombre} con éxito",
        "datos": {
            "id": paciente.id,
            "nombre": paciente.nombre,
            "apellido": paciente.apellido,
            "edad": paciente.edad,
            "contacto": paciente.contacto,
            "alergias": paciente.alergias,
            "activo": paciente.activo,
            
        }
    
    }
   
    
            

# devuelve la lista de todos los pacientes
@app.get("/pacientes")
def ver_pacientes():
    return {
        "pacientes": pacientes_db
    }



# devuelve un paciente especifico    
@app.get("/pacientes/{contador_id}")
def ver_paciente(contador_id = int):
    for i in pacientes_db:
        if i["id"] == contador_id:
            return i

"""

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