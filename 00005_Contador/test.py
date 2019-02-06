class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertEquals(contador, 8, 'El valor de contador no es correcto')
    
  def test_iteracion(self):
    self.assertTrue(isinstance(n, (int)), 'Tiene que existir la asignacion de los valores a n durante la iteracion.')
    self.assertTrue(n==6)