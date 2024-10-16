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
