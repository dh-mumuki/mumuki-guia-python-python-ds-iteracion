class TestFixtures(unittest.TestCase):
  def test_listas(self):
    
    def estan_los_cuadrados(lista, cuadrados):
      
      for x in lista:
        if not x**2 in cuadrados:
          return False
      
      return True
      
    self.assertTrue(estan_los_cuadrados(lista,cuadrados), 'Al menos un elemento no es un cuadrado.')
