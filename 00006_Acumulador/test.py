class TestFixtures(unittest.TestCase):
  def test_sumatoria(self):
    self.assertTrue(isinstance(sumatoria,(int, float)), 'El valor de la sumatoria no es numerico')
    self.assertEquals(sumatoria, 42, 'El valor de sumatoria es incorrecto.')
    
  def test_iteracion(self):
    self.assertTrue(isinstance(n, (int)), 'Tiene que existir la asignacion de los valores a n durante la iteracion.')
    self.assertTrue(n==6)