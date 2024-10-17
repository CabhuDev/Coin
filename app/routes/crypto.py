#Define la lógica del endpoint para obtener el precio de Ethereum.
#Utiliza el servicio coinmarket.py para realizar las llamadas a la API.

from fastapi import APIRouter  
from fastapi.responses import JSONResponse  # Importa JSONResponse para devolver respuestas en formato JSON
from app.services.coinmarketcap import get_eth_price,get_btc_price  # Importa la función get_eth_price y get_btc_price para obtener el precio de Ethereum desde un servicio externo

# Crear un router para definir las rutas relacionadas con 'crypto'
router = APIRouter()

@router.get("/get_eth_price", response_class=JSONResponse)  # Define una ruta GET para obtener el precio de Ethereum, devolviendo una respuesta JSON
async def get_eth_price_endpoint():
    # Llama a la función get_eth_price para obtener el precio de Ethereum
    eth_price = get_eth_price()
    
    # Verifica si se pudo obtener el precio correctamente
    if eth_price is not None:
        # Devuelve el precio de Ethereum en formato JSON si no hubo errores
        return JSONResponse(content={'eth_price': eth_price})
    else:
        # Devuelve un mensaje de error si no se pudo obtener el precio
        return JSONResponse(content={'error': 'Error al obtener el precio de Ethereum.'})
    
@router.get("/get_btc_price", response_class=JSONResponse)  # Define una ruta GET para obtener el precio de Bitcoin, devolviendo una respuesta JSON
async def get_btc_price_endpoint():
    # Llama a la función get_btc_price para obtener el precio de Bitcoin
    btc_price = get_btc_price()
    
    # Verifica si se pudo obtener el precio correctamente
    if btc_price is not None:
        # Devuelve el precio de Bitcoin en formato JSON si no hubo errores
        return JSONResponse(content={'btc_price': btc_price})
    else:
        # Devuelve un mensaje de error si no se pudo obtener el precio
        return JSONResponse(content={'error': 'Error al obtener el precio de Bitcoin.'})
