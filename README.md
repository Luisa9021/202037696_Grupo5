# 202037696_Grupo5

Sistema integrado de control y diccionarios de datos para automatización
industrial, desarrollado en Python como parte del curso **Lenguajes
Interpretados (202037696)** de la Universidad Nacional Abierta y a
Distancia (UNAD), bajo la metodología de Aprendizaje Basado en Retos (ABR).

## Estructura

| Ruta | Contenido |
|------|-----------|
| `src/main.py` | Menú principal que integra los tres módulos |
| `src/control/bombeo.py` | Control del sistema de bombeo hidroeléctrico (Tarea 2) |
| `src/datos/mapa_bme680.py` | Diccionario de registros del BME680 y consulta segura (Tarea 3) |
| `src/optimizacion/` | Filtro PT100 optimizado y comparación de CPU (Tarea 4) |
| `tests/` | Pruebas automáticas de los módulos |
| `docs/metricas_cpu.md` | Tiempos de CPU antes y después de la optimización |

## Ejecución

Requiere Python 3.10 o superior. Desde la raíz del repositorio:

    python -m src.main

Para correr las pruebas:

    python -m unittest discover -s tests -t .

## Convenciones de estilo (PEP 8)

- Indentación de 4 espacios
- Variables y funciones en `snake_case`
- Máximo 79 caracteres por línea
- Verificación: `flake8 src tests`

## Resultados de optimización

El filtro del transductor PT100 pasó de complejidad O(N²) a O(N). Con 10.000
lecturas, el tiempo medido con `time.perf_counter()` bajó de 2861,818 ms a
2,931 ms (99,90 % menos). Detalle en `docs/metricas_cpu.md`.

## Roles

| Rol | Integrante |
|-----|-----------|
| Líder de Integración | Luisa Viviana Rueda Ayala |
| Auditor PEP 8 | Disponible |
| Redactor Técnico | Disponible |
| Revisor de Calidad | Disponible |
