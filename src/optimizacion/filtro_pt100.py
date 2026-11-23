"""Filtro de ruido termico para el transductor RTD PT100 (Tarea 4).

Calcula el promedio movil acumulado con una suma acumulada, lo que reduce
la complejidad temporal de O(N^2) a O(N) sin alterar los resultados.
"""

PT100_TEMPERATURA_MINIMA = -200.0
PT100_TEMPERATURA_MAXIMA = 850.0


def validar_rango_pt100(temperaturas):
    """Emite una alerta si hay lecturas fuera del rango del PT100."""
    fuera_de_rango = [
        t for t in temperaturas
        if not PT100_TEMPERATURA_MINIMA <= t <= PT100_TEMPERATURA_MAXIMA
    ]
    if fuera_de_rango:
        print(f"ALERTA: {len(fuera_de_rango)} lecturas fuera de rango.")


def filtrar_ruido_termico(temperaturas):
    """Calcula el promedio móvil acumulado de las temperaturas."""
    validar_rango_pt100(temperaturas)
    temperaturas_filtradas = []
    suma_acumulada = 0

    for cantidad, temperatura in enumerate(temperaturas, start=1):
        suma_acumulada += temperatura
        temperaturas_filtradas.append(suma_acumulada / cantidad)

    return temperaturas_filtradas
