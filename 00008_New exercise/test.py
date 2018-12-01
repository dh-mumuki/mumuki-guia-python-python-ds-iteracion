class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertEquals(nombre.lower(),  "eugenia")
    
  def test_listas(self):
    self.assertEquals(saludos, ["Hola Angeles!", "Hola Carla!", "Hola Natalia!", "Hola Eugenia!"])

  def test_listas(self):
    self.assertTrue('append' in '/*...content...*/')