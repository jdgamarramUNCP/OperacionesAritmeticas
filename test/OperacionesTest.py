import unittest
from scr.OperacionesAritmeticas import OperacionesAritmeticas

class OperacionesTest ( unittest.TestCase ) :
    def setUp(self) :
       self.operacion = OperacionesAritmeticas()

    def tearDown(self):
        self.operacion = None
    def test_sumar_int_y_int ( self ) :
        self.assertEqual (12, self.operacion.operacionSuma (5, 7))

    def test_sumar_float_y_float ( self ) :
        self.assertEqual (12.8, self.operacion.operacionSuma (5.5, 7.3))

    def test_1_noPuedo_sumar_int_y_str ( self ) :
        self.assertEqual (12, self.operacion.operacionSuma (5, 7))
        with self.assertRaises(ValueError):
            self.operacion.operacionSuma ("5", 7)

    def test_2_noPuedo_sumar_int_y_str(self):
        self.assertEqual (12, self.operacion.operacionSuma (5, 7))
        self.assertRaises(ValueError, self.operacion.operacionSuma, "5", 7)

    def test_3_noPuedo_sumar_int_y_str ( self ) :
        self.assertRaises (TypeError, Operaciones.operacionSuma, 1, '1')

    def test_4_noPuedo_sumar_int_y_str ( self ) :
        with self.assertRaises ( TypeError ) :
            1 + '1'

    def test_5_noPuedo_sumar_int_y_str(self):
        self.assertEqual(12, self.operacion.operacionSuma(5, 7))
        with self.assertRaises(ValueError):
            self.operacion.operacionSuma("a", 4)