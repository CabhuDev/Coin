# Archivo principal para ejecutar la aplicación (contiene la instancia de FastAPI)



from fastapi import FastAPI
from app.routes import home,crypto
from fastapi.staticfiles import StaticFiles

# Crea una instancia de FastAPI para manejar solicitudes y respuestas
app = FastAPI()

# Monta la carpeta "static" para servir archivos estáticos (JavaScript, CSS, imágenes, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Registrar rutas
# Registra las rutas definidas en el módulo 'home' y 'crypto' con la aplicación principal
# Esto permite que la aplicación incluya todas las rutas (endpoints) especificadas en 'home.router'
app.include_router(home.router)

# Esto hace que todos los endpoints relacionados con criptomonedas estén disponibles en la aplicación principal
app.include_router(crypto.router)



# Ejecuta el servidor utilizando uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)