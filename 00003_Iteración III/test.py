class TestFixtures(unittest.TestCase):
  def test_cuadrados(self):
    self.assertTrue(cuadrados(lista), [4, 16, 4, 25 , 64, 1, 9]), 'Al menos un elemento no es un cuadrado.')
