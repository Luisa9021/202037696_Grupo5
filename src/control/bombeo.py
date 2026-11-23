"""Control del sistema de bombeo hidroelectrico (Escenario 3, Tarea 2).

El nivel del tanque, expresado en porcentaje, determina el estado de la
bomba. Los niveles exactos de 0 % y 100 % se tratan como falla del sensor.
"""

NIVEL_FALLA_MINIMO = 0
NIVEL_FALLA_MAXIMO = 100
NIVEL_BAJO = 15
NIVEL_ALTO = 85
INCREMENTO_NIVEL_BAJO = 5
INCREMENTO_NIVEL_NORMAL = 2
MAX_LECTURAS = 20


def simular_bombeo(nivel_inicial=10, max_lecturas=MAX_LECTURAS):
    """Simula el monitoreo del tanque y retorna el nivel final.

    El ciclo se limita a ``max_lecturas`` para evitar bucles infinitos.
    """
    nivel = nivel_inicial
    monitoreo = True
    lecturas = 0

    while monitoreo and lecturas < max_lecturas:
        print(f"Nivel actual: {nivel}%")

        if nivel in (NIVEL_FALLA_MINIMO, NIVEL_FALLA_MAXIMO):
            print("ERROR: Falla de lectura del sensor")
            monitoreo = False

        elif nivel < NIVEL_BAJO:
            print("Control: Bomba encendida - Nivel bajo")
            nivel += INCREMENTO_NIVEL_BAJO

        elif NIVEL_BAJO <= nivel <= NIVEL_ALTO:
            print("Control: Operación hidráulica normal")
            nivel += INCREMENTO_NIVEL_NORMAL

        else:
            print("Control: Bomba apagada - Tanque lleno")
            monitoreo = False

        lecturas += 1

    print("Monitoreo finalizado")
    return nivel
