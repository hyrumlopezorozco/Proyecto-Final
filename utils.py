"""
main.py -  
Hyrum , 11/3/2026
Delside Manjarrez
"""

import math
def calcular_distancia_haversine(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia entre dos puntos geográficos usando la fórmula de Haversine.
    
    Parámetros:
    lat1, lon1: Coordenadas del primer punto (en grados).
    lat2, lon2: Coordenadas del segundo punto (en grados).
    
    Retorna:
    Distancia en kilómetros entre los dos puntos.
    """
    # Convertir grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Diferencias de coordenadas
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Radio de la Tierra en kilómetros
    radio_tierra_km = 6371.0
def dar_formato_tiempo(segundos):
    """
    Convierte un tiempo en segundos a un formato legible de horas, minutos y segundos.
    """
    horas = segundos // 3600        
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60      
    
    # Distancia final
    distancia_km = radio_tierra_km * c
    return distancia_km