class TestFixtures(unittest.TestCase):
  
  def test_listas(self):
    self.assertFalse(False in (set([x for x in profesores_dh if x in ('Pablo', 'Demian', 'Paolo', 'Julián')])), 'Falta algun nombre en la lista')
    
  def test_iteracion(self):
    self.assertTrue(nombre=='Julian', 'La iteracion no se realizo correctamente.')