import unittest
from src.logica.OperacionesAritmeticas import OperacionesAritmeticas

class TestOperacionesAritmeticas(unittest.TestCase):
    def setUp(self):
        self.operacion = OperacionesAritmeticas()

    def tearDown(self):
        self.operacion = None

    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        sumando1 = 4
        sumando2 = 5
        resultadoEsperado = 9

        # Do
        resultadoActual = self.operacion.suma(sumando1, sumando2)

        # Assert
        self.assertEqual(resultadoEsperado,resultadoActual)

    def test_suma_dosNumeros_retornaSumaCorrecta(self):
        self.assertEqual(4,self.operacion.suma(2,2))

