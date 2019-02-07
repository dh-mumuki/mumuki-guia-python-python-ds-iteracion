class TestFixtures(unittest.TestCase):
  def test_media(self):
    self.assertTrue(media==5, 'El valor de media no es correcto')

  def test_contador(self):
    self.assertEquals(contador, 8, 'El valor contador no es correcto')
    
  def test_suma(self):
    self.assertEquals(sumatoria, 42, 'El valor de la suma no es correcto')
    
  def test_iteracion(self):
    self.assertTrue('n' in globals() , 'La iteracion no es correcta')