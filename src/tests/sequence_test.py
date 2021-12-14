import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sovellus import sequence
from sovellus import gc_content

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/testitiedosto.txt')
DOTPLOTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/dotplotdata.txt')

class TestSequence(unittest.TestCase):

    def setUp(self):
        self.seq = sequence.Sequence()

    def test_dotplot(self):
        """
        Testaa Sequence-luokan dotplot-funktion toimivuutta testitiedostolla.
        Args:
            None

        Returns:
             assertEqual: testaa, toimiiko funktio oikein.
        """

        self.assertEqual(self.seq.dotplot(DOTPLOTDATA_FILENAME), True)
