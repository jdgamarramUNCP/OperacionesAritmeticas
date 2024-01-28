import unittest

from scr.OperacionesAritmeticas import OperacionesAritmeticas


class PruebaSuma(unittest.TestCase):
    def setUp(self):
        self.suma = OperacionesAritmeticas()

    def tearDown(self):
        self.suma = None

    def test_suma_dosNumeros_retornaSumaNumeros(self):
        # Arrange
        sumando1 = 4
        sumando2 = 5
        resultadoEsperado = 9

        # Do
        resultadoActual = self.suma.operacionSuma(sumando1, sumando2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_suma_dosNumerosNegativos_retornaSumaNumeros(self):
        # Arrange
        sumando1 = -4
        sumando2 = -5
        resultadoEsperado = -9

        # Do
        resultadoActual = self.suma.operacionSuma(sumando1, sumando2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)


    def test_suma_sumandoNoNumerico_lanzaExcepcion(self):
        self.assertEqual(12, self.suma.operacionSuma(5, 7))
        with self.assertRaises(ValueError):
            self.suma.operacionSuma("a", 5)
