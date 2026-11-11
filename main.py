"""
main.py -  
Hyrum , 11/3/2026
Delside Manjarrez
"""

import api
import utils

def mostrar_menu():
    print("\n=============================================")
    print("   SISTEMA DE GESTIÓN DE RECURSOS COMUNITARIOS")
    print("=============================================")
    print("1. Buscar recursos disponibles por Código Postal")
    print("2. Registrar beneficiario o solicitud de ayuda")
    print("3. Calcular distancias a centros de atención")
    print("4. Salir")
    print("=============================================")

def ejecutar_sistema():
    print("\n=== Bienvenido al Sistema de Apoyo Comunitario ===")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            print("\n--- BÚSQUEDA DE RECURSOS COMUNITARIOS ---")
            cp = input("Ingrese el código postal de la zona: ").strip()
            categoria = input("Tipo de ayuda (Vivienda, Comida, Empleo, Servicios): ").strip()
            
            print(f"\n[Info] Resumen de búsqueda -> CP: {cp} | Categoría: {categoria}")
            print("Consultando bases de datos comunitarias...")
            
            try:
                # Llamada al módulo de API para extraer recursos habitacionales o alimentarios
                recursos = api.buscar_recursos_por_cp(cp, category=categoria)
                print(recursos)
            except Exception as e:
                print(f"Error al consultar recursos comunitarios: {e}")
                
        elif opcion == "2":
            print("\n--- REGISTRO DE SOLICITUD DE ASISTENCIA ---")
            nombre_anonimo = input("Ingrese un alias o ID único (No datos reales): ").strip()
            tipo_necesidad = input("Describa brevemente la necesidad prioritaria: ").strip()
            
            try:
                # Simulación de guardado en el sistema de gestión de casos
                print("\nProcesando registro en el portal de ayuda...")
                resultado = api.registrar_solicitud(nombre_anonimo, tipo_necesidad)
                print(resultado)
            except Exception as e:
                print(f"Error al procesar la solicitud en el sistema: {e}")
                
        elif opcion == "3":
            print("\n--- CÁLCULO DE DISTANCIA A CENTROS DE AYUDA ---")
            print("Calcule la distancia hacia el refugio, banco de comida o agencia más cercana.")
            # Coordenadas de ejemplo (latitud, longitud)
            try:
                lat1 = float(input("Latitud actual del usuario: "))
                lon1 = float(input("Longitud actual del usuario: "))
                lat2 = float(input("Latitud del centro de asistencia: "))
                lon2 = float(input("Longitud del centro de asistencia: "))
                
                distancia = utils.calcular_distancia_haversine(lat1, lon1, lat2, lon2)
                print(f"\n[Resultado] La distancia al centro de ayuda es de: {distancia:.2f} km")
            except ValueError:
                print("Error: Por favor, ingrese valores numéricos válidos para las coordenadas.")
            except Exception as e:
                print(f"Error inesperado en el cálculo: {e}")
                
        elif opcion == "4":
            print("\n¡Gracias por trabajar en favor de la comunidad! Cerrando sistema.")
            break
        else:
            print("\n[Alerta] Opción no válida. Por favor, seleccione un número del 1 al 4.")

if __name__ == "__main__":
    ejecutar_sistema()