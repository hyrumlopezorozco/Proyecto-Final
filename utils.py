import math
def calcular_distancia(latitud1, longitud1, latitud2, longitud2):
    # Convertir radiosde tierra en  kilómetros
    radio_tierra = 6371.0
    # Convertir grados a radianes
    lat1_rad = math.radians(latitud1)
    lon1_rad = math.radians(longitud1)
    lat2_rad = math.radians(latitud2)
    lon2_rad = math.radians(longitud2)

    # Calcular la diferencias entre las coordenadas
    diferencia_lat = lat2_rad - lat1_rad
    diferencia_lon = lon2_rad - lon1_rad

    # Fórmula de Haversine
    componente_a = math.sin(diferencia_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(diferencia_lon / 2)**2
    componente_c = 2 * math.atan2(math.sqrt(componente_a), math.sqrt(1 - componente_a))
    #calcular y devolverla distancia final en kilómetros
    distancia = radio_tierra * componente_c
    return distancia_kilometros