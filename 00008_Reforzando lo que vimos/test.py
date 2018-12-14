class TestFixtures(unittest.TestCase):
  
  
  
  def test_listas(self):
    saludos_test = ["Hola " + x + "!" for x in nombres]
    self.assertEquals(len(saludos_test), len(saludos))