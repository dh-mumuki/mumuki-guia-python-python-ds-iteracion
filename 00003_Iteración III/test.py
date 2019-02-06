class TestFixtures(unittest.TestCase):
  def test_listas(self):
    
    def estan_los_cuadrados(lista1, cuadrados):
      
      for x in lista1:
        if not x**2 in cuadrados:
          return False
      
      return True
      
    self.assertTrue(estan_los_cuadrados(lista1,cuadrados), 'Los elementos no son el cuadrado de los numeros dados')
