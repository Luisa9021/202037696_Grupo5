"""Pruebas basicas de los tres modulos integrados."""

import unittest

from src.control.bombeo import simular_bombeo
from src.datos.mapa_bme680 import MAPA_BME680, consulta_interactiva
from src.datos.mapa_bme680 import consultar_registro
from src.optimizacion.benchmark import filtrar_ruido_termico_cuadratico
from src.optimizacion.filtro_pt100 import filtrar_ruido_termico


class PruebasBombeo(unittest.TestCase):
    """Verifica la logica de control del tanque."""

    def test_limita_las_lecturas(self):
        self.assertEqual(simular_bombeo(nivel_inicial=10), 53)

    def test_falla_de_sensor_detiene_el_ciclo(self):
        self.assertEqual(simular_bombeo(nivel_inicial=0), 0)

    def test_tanque_lleno_detiene_el_ciclo(self):
        self.assertEqual(simular_bombeo(nivel_inicial=90), 90)


class PruebasMapaBme680(unittest.TestCase):
    """Verifica las consultas seguras al diccionario."""

    def test_registro_existente(self):
        self.assertEqual(consultar_registro("0x60"), MAPA_BME680["0x60"])

    def test_registro_inexistente_retorna_none(self):
        self.assertIsNone(consultar_registro("0x99"))

    def test_limite_de_intentos(self):
        respuestas = iter(["0x99", "0x99", "0x99"])
        resultado = consulta_interactiva(entrada=lambda _: next(respuestas))
        self.assertIsNone(resultado)

    def test_encuentra_en_el_segundo_intento(self):
        respuestas = iter(["0x99", "0x61"])
        resultado = consulta_interactiva(entrada=lambda _: next(respuestas))
        self.assertEqual(resultado, MAPA_BME680["0x61"])


class PruebasFiltroPt100(unittest.TestCase):
    """Verifica que la version optimizada no altera los resultados."""

    def test_resultados_identicos_a_la_version_original(self):
        lecturas = [110.5, 112.3, 115.8, 111.2, 118.4] * 40
        self.assertEqual(
            filtrar_ruido_termico(lecturas),
            filtrar_ruido_termico_cuadratico(lecturas),
        )


if __name__ == "__main__":
    unittest.main()
