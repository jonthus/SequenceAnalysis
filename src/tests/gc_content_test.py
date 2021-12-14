import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sovellus import sequence
from sovellus import gc_content

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/lukutesti.txt')
HIIRI_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/hiiri.txt')

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
