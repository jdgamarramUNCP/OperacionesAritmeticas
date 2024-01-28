import unittest
from scr.OperacionesAritmeticas import OperacionesAritmeticas

class PruebaSuma(unittest.TestCase):
    def test_suma_dosNumeros_retornaSumaNumeros(self):
        # Arrange
        suma = OperacionesAritmeticas()
        sumando1 = 4
        sumando2 = 5
        resultadoEsperado = 9

        # Do
        resultadoActual = suma.suma(sumando1, sumando2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)
