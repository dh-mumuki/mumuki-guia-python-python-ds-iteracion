class TestFixtures(unittest.TestCase):
  
  saludos_test = ["Hola " + x + "!" for x in nombres]
  
  def test_listas(self):
    self.assertEquals(len(saludos_test), len(saludos))