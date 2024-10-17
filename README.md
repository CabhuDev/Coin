# Crypto Prices App

Este proyecto es una aplicación sencilla desarrollada con **FastAPI** que permite consultar el precio actual de **Ethereum (ETH)** y **Bitcoin (BTC)** en tiempo real. La aplicación incluye un front-end con HTML y JavaScript para interactuar con el usuario, así como un back-end que se comunica con una API externa para obtener los precios de las criptomonedas.

## Características
- Consultar el precio actual de Ethereum y Bitcoin.
- Interfaz de usuario sencilla creada con HTML y CSS.
- Documentación de la API generada automáticamente con **Swagger UI** y **ReDoc**.

## Tecnologías Utilizadas
- **FastAPI**: Framework para el back-end.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.
- **HTML5, CSS3 y JavaScript**: Para la interfaz de usuario.
- **Jinja2**: Para la renderización de plantillas HTML.

## Requisitos Previos
- **Python 3.7+** instalado.
- **pip** (gestor de paquetes de Python).

## Instalación
1. Clona el repositorio en tu máquina local:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Coin
   ```

2. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución del Servidor
Para iniciar el servidor localmente, sigue estos pasos:

1. Navega al directorio del proyecto.

2. Ejecuta el siguiente comando para iniciar el servidor con **Uvicorn**:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Abre tu navegador y navega a `http://127.0.0.1:8000` para ver la aplicación en funcionamiento.

## Documentación de la API
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Estas interfaces proporcionan una descripción interactiva de los endpoints de la API y permiten realizar pruebas fácilmente.

## Estructura del Proyecto
```
Coin/
├── app/
│   ├── main.py           # Archivo principal para ejecutar la aplicación FastAPI
│   ├── routes/
│   │   ├── home.py       # Definición de rutas relacionadas con la página principal
│   │   └── crypto.py     # Definición de rutas para precios de criptomonedas
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css # Archivo CSS para el estilo de la página
│   │   └── js/
│   │       └── script.js # Archivo JavaScript para manejar la lógica del front-end
│   ├── templates/
│   │   └── index.html    # Plantilla HTML principal
└── requirements.txt      # Archivo con las dependencias del proyecto
```

## Uso
- **Obtener Precio de ETH**: Presiona el botón "Obtener precio de ETH" para consultar el precio actual de Ethereum.
- **Obtener Precio de BTC**: Presiona el botón "Obtener precio de BTC" para consultar el precio actual de Bitcoin.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor abre un **pull request** con tus mejoras o soluciones a problemas.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Puedes consultar el archivo `LICENSE` para obtener más detalles.


crypto_app/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Archivo principal para ejecutar la aplicación (contiene la instancia de FastAPI)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── home.py            # Ruta principal para la página HTML
│   │   └── crypto.py          # Ruta que maneja la lógica de precios de criptomonedas
│   ├── services/
│   │   ├── __init__.py
│   │   └── coinmarket.py      # Lógica para interactuar con la API de CoinMarketCap
│   ├── templates/
│   │   └── index.html         # Archivo HTML para la página principal
│   └── static/
│       └── js/
│           └── script.js      # Archivo JavaScript para manejar la interacción en el frontend
│
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Información sobre el proyecto


**Resumen**
1. Instala FastAPI y Uvicorn:
    python -m pip install fastapi uvicorn
2. Ejecuta el servidor:
    python -m uvicorn app.main:app --reload
3. Abre un navegador y visita http://127.0.0.1:8000 para ver la aplicación funcionando.
   
