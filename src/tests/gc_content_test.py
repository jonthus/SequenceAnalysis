import unittest
import gc_content
import os

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'lukutesti.txt')
HIIRI_FILENAME = os.path.join(os.path.dirname(__file__), 'hiiri.txt')

class TestGcContent(unittest.TestCase):

    def test_percentages(self):
        """
        Testaa GC_content luokan prosenttien laskemista.
        Args:
            None
        Returns:
            assertEqual: vertaa merkkijonoja, palauttaa True jos samat.
        """
        testdata = 'GCGCABAB'
        self.assertEqual(gc_content.percentages(testdata), 50.0)

    def test_gc_content(self):
        """
        Testaa GC_content luokan tiedoston lukemista.
        Args:
            None55.53250345781466

        Returns:
             assertEqual: testaa, toimiiko funktio oikein.
        """
        self.assertEqual(gc_content.parseContent(TESTDATA_FILENAME), 55.53250345781466)


# EOF
