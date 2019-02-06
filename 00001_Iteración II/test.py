class TestFixtures(unittest.TestCase):
  
  def test_listas(self):
    self.assertFalse(False in (set([x for x in profesores_dh if x in ('Pablo', 'Demian', 'Paolo', 'Julian')])), 'Falta algun nombre en la lista')