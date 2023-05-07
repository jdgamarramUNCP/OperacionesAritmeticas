import unittest
from src.logica.OperacionesAritmeticas import OperacionesAritmeticas

class TestOperacionesAritmeticas(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operacion = OperacionesAritmeticas()
        sumando1 = 4
        sumando2 = 5
        resultadoEsperado = 9

        # Do
        resultadoActual = operacion.suma(sumando1, sumando2)

        # Assert
        self.assertEqual(resultadoEsperado,resultadoActual)

    def test_suma_dosNumeros_retornaSumaCorrecta(self):
        suma = OperacionesAritmeticas()
        self.assertEqual(4,suma.suma(2,2))

