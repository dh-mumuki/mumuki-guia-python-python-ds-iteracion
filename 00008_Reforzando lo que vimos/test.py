class TestFixtures(unittest.TestCase):
  
  def test_contenido(self):
    
    def f(saludos_test, saludos):
      for i in saludos:
        if i not in saludos_test:
          return False
      for i in saludos_test:
        if i not in saludos:
          return False
      return True
    self.assertTrue(f(saludos_test, saludos), "Algun saludo no es correcto o se repite")
  
  def test_listas(self):
    saludos_test = ["Hola " + x + "!" for x in nombres]
    self.assertEquals(len(saludos_test), len(saludos))