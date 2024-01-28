class OperacionesAritmeticas:
    def operacionSuma(self, sumando1, sumando2):
        for n in (sumando1, sumando2):
            if not isinstance(n, int) and not isinstance(n, float):
                raise ValueError
        return sumando1 + sumando2