import unittest
from adivinanumeros import Adivinar

#Actualemnte no funciona
class MisTests(unittest.TestCase):

    def setUp(self):
        self.adivinanumeros = Adivinar()
        self.adivinanumeros.Adivinar.juego.secreto= 55

    def test_resultado_menor(self):
        resultado = self.adivinanumeros.juego.secreto(20)
        self.assertEqual(resultado,'Mi numero es menor, intentelo denuevo:')

    def test_resultado_mayor(self):
        resultado = self.adivinanumeros.juego.secreto(60)
        self.assertEqual(resultado,'Mi numero es mayor, intentelo denuevo:')

    def test_igual(self):
        resultado = self.adivinanumeros.juego.secreto(55)
        self.assertEqual(resultado,"Exelente, le acertaste a mi numero\n")




if __name__ == '__main__':
    unittest.main()




