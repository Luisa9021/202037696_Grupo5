"""Punto de entrada del sistema integrado (202037696_Grupo5).

Ejecucion: ``python -m src.main``
"""

from src.control.bombeo import simular_bombeo
from src.datos.mapa_bme680 import consulta_interactiva
from src.optimizacion.benchmark import comparar

MENU = """
=== Sistema integrado de automatización industrial ===
1. Control de bombeo hidroeléctrico (Tarea 2)
2. Consulta de registros del BME680 (Tarea 3)
3. Comparación de CPU del filtro PT100 (Tarea 4)
4. Salir
"""


def main():
    """Muestra el menú y ejecuta el módulo elegido."""
    acciones = {
        "1": simular_bombeo,
        "2": consulta_interactiva,
        "3": comparar,
    }

    while True:
        print(MENU)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "4":
            print("Sistema finalizado.")
            break

        accion = acciones.get(opcion)
        if accion is None:
            print("Opción no válida.")
        else:
            accion()


if __name__ == "__main__":
    main()
