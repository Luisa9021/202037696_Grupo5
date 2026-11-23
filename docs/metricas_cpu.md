# Métricas de CPU - Filtro PT100 (Escenario 2, Tarea 4)

Entrada: 10.000 lecturas. Medición en Google Colab.

| Método de medición | Código original | Código optimizado | Reducción |
|--------------------|-----------------|-------------------|-----------|
| `time.perf_counter()` | 2861,818 ms | 2,931 ms | 99,90 % |
| `%timeit` (3 rondas) | 3,52 s ± 862 ms | 2,07 ms ± 357 µs | 99,94 % |

Complejidad: de O(N²) (unas 50 millones de sumas) a O(N) (10.000 sumas).
Para reproducir la comparación desde la raíz del repositorio:

    python -c "from src.optimizacion import benchmark; benchmark.comparar()"
