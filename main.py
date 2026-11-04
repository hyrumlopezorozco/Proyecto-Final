"""
main.py -  
Hyrum , 11/3/2026

"""

# 1. Menú principal
# Pueden agregar más opciones después
print("\n=== Mensaje de bienvenida ===")
print("1. Calcular distancia")
print("2. Salir")

# 2. Pedir al usuario que elija una opción del menú
opcion = input("Elige una opción: ")

# 3. Si elige 1 pedir origen y destino; elif salida adiós.
# 4. Dentro del 1 tenemos que pedir ciudad origen y destino.
# 5. Luego calcular la distancia... ¿cómo? coordenadas.
# 6. try except

if opcion == "1":

    # Entrada de datos del usuario
    ciudad_o = input("Ciudad de origen: ")

    # Mostrar resumen
    print("\n--- Resumen ---")
    print(f"Origen: {ciudad_o}")

    # Consulta a la API
    print("Consultando datos...")

    # --- BÚSQUEDA DE ORIGEN CON TRY/EXCEPT ---


    # Resultados
    print("\n--- Coordenadas Obtenidas ---")

    # Destino hard coded
    print("Destino: San Marcos, Guatemala - lat 14.96")
    print("Distancia:")


elif opcion == "2":
    print("¡Hasta pronto!")

else:
    print("Opción no válida.")