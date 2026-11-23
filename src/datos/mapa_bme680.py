"""Diccionario de registros del sensor BME680 (Escenario 1, Tarea 3).

Cada direccion hexadecimal es una clave unica y contiene las subclaves
``status``, ``calib_val`` y ``limit``.
"""

MAX_INTENTOS = 3

MAPA_BME680 = {
    "0x60": {
        "status": True,
        "calib_val": 12,
        "limit": 100,
    },
    "0x61": {
        "status": True,
        "calib_val": 55,
        "limit": 200,
    },
    "0x62": {
        "status": False,
        "calib_val": 88,
        "limit": 90,
    },
}


def consultar_registro(direccion, mapa=None):
    """Retorna el registro de ``direccion`` o None si no existe.

    Usa ``dict.get`` para evitar KeyError ante direcciones inexistentes.
    """
    if mapa is None:
        mapa = MAPA_BME680
    return mapa.get(direccion)


def mostrar_registro(registro):
    """Imprime los campos de un registro del mapa."""
    print("\nRegistro encontrado:")
    print("status:", registro.get("status"))
    print("calib_val:", registro.get("calib_val"))
    print("limit:", registro.get("limit"))


def consulta_interactiva(max_intentos=MAX_INTENTOS, entrada=input):
    """Pide direcciones hasta encontrar una o agotar los intentos.

    Retorna el registro encontrado o None si se alcanzo el limite.
    """
    intentos = max_intentos

    while intentos > 0:
        direccion = entrada("Ingrese una dirección hexadecimal: ")
        registro = consultar_registro(direccion)

        if registro is not None:
            mostrar_registro(registro)
            return registro

        print("\nNo se encontró el registro:", direccion)
        intentos -= 1
        print("Intentos restantes:", intentos)

    print("\nSe alcanzó el límite de consultas.")
    return None
