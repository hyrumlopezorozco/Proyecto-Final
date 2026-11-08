
import requests

headers = {
    "User-Agent": "LocalHelp/1.0"
}

def obtener_coordenadas(ciudad):

    parametros = {
        "q": ciudad,
        "format": "jsonv2",
        "limit": 1
    }

    respuesta = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params=parametros,
        headers=headers,
        timeout=20
    )

    respuesta.raise_for_status()
    datos = respuesta.json()

    if not datos:
        return None

    latitud = float(datos[0]["lat"])
    longitud = float(datos[0]["lon"])

    return latitud, longitud
