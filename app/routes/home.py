# Contiene la lógica para mostrar la página principal.

from fastapi import APIRouter  # Importa APIRouter para definir y manejar rutas de forma modular
from fastapi.responses import HTMLResponse  # Importa HTMLResponse para devolver respuestas HTML
from fastapi.templating import Jinja2Templates  # Importa Jinja2Templates para trabajar con plantillas HTML
"""Jinja2Templates facilita la generación de contenido HTML dinámico. 
En el código proporcionado, se está utilizando para renderizar el archivo index.html, 
proporcionando datos como el objeto request que la plantilla puede utilizar. """

from starlette.requests import Request  # Importa Request para acceder a los detalles de la solicitud

# Crear un router para definir las rutas relacionadas con 'home'
router = APIRouter()

# Configurar Jinja2 para trabajar con plantillas desde el directorio especificado
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)  # Define una ruta GET para la página de inicio, devolviendo una respuesta HTML
async def get_home(request: Request):
    # Renderiza la plantilla 'index.html' (escrita en HTML5) y le pasa el objeto de solicitud para su uso en la plantilla
    return templates.TemplateResponse("index.html", {"request": request})

