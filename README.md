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
4. 
C:\Users\Pablo\iCloudDrive\1.1Programación\Python