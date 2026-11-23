"""Medicion de tiempo de CPU: version original (O(N^2)) vs optimizada."""

import time

from src.optimizacion.filtro_pt100 import filtrar_ruido_termico

LECTURAS_BASE = [110.5, 112.3, 115.8, 111.2, 118.4]
REPETICIONES = 2000


def filtrar_ruido_termico_cuadratico(temperaturas):
    """Version original ineficiente, conservada solo como referencia.

    Recalcula la suma completa desde cero en cada posicion: O(N^2).
    """
    temperaturas_filtradas = []

    for i in range(len(temperaturas)):
        suma_temporal = 0
        for j in range(0, i + 1):
            suma_temporal = suma_temporal + temperaturas[j]
        promedio = suma_temporal / (i + 1)
        temperaturas_filtradas.append(promedio)

    return temperaturas_filtradas


def medir_tiempo_ms(funcion, *argumentos):
    """Ejecuta ``funcion`` y retorna (resultado, milisegundos)."""
    inicio = time.perf_counter()
    resultado = funcion(*argumentos)
    fin = time.perf_counter()
    return resultado, (fin - inicio) * 1000


def comparar(repeticiones=REPETICIONES):
    """Compara ambas versiones con ``5 * repeticiones`` lecturas."""
    lecturas = LECTURAS_BASE * repeticiones

    original, ms_original = medir_tiempo_ms(
        filtrar_ruido_termico_cuadratico, lecturas
    )
    optimizado, ms_optimizado = medir_tiempo_ms(
        filtrar_ruido_termico, lecturas
    )

    print(f"Lecturas procesadas: {len(lecturas)}")
    print(f"Tiempo original: {ms_original:.3f} ms")
    print(f"Tiempo optimizado: {ms_optimizado:.3f} ms")
    print(f"Resultados idénticos: {original == optimizado}")
    return ms_original, ms_optimizado
