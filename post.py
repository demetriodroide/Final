from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista para almacenar los libros
libros_creados = []

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int

@app.post("/libros")
async def crear_libro(libro: Libro):
    # Guardar el libro en la lista
    libros_creados.append(libro.model_dump())
    
    return {
        "mensaje": f"Se ha creado el libro {libro.titulo} con éxito",
        "datos": {
            "titulo": libro.titulo,
            "autor": libro.autor,
            "paginas": libro.paginas
        }
    }


@app.get("/libros")
def ver_libros():
    return {
        "total": len(libros_creados),
        "libros": libros_creados
    }
    