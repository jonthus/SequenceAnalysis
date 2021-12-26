import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services import gc_service
from entities import gc_content

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/lukutesti.txt')

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

    def test_GcService(self):
        """
        Testaa GcService luokan tiedoston suorittamista.
        Args:
            None

        Returns:
             assertEqual: testaa, toimiiko funktio oikein.
        """
        self.assertEqual(gc_service.gc_run(TESTDATA_FILENAME), 55.53250345781466)


# EOF
