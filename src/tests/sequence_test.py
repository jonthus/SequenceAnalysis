import unittest
import os
from sequence import Sequence

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testitiedosto.txt')
DOTPLOTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'dotplotdata.txt')

class TestSequence(unittest.TestCase):

    def setUp(self):
        self.seq = Sequence()
        self.testdata = self.seq.parse(TESTDATA_FILENAME)

    def test_parse(self):
        """
        Testaa Sequence-luokan parse-funktion toimivuutta testitiedostolla.
        Args:
            None
        Returns:
            assertEqual: vertaa merkkijonoja, palauttaa True jos samat.
        """
        self.assertEqual(self.testdata, "this file has content")

    def test_dotplot(self):
        """
        Testaa Sequence-luokan dotplot-funktion toimivuutta testitiedostolla.
        Args:
            None

        Returns:
             assertEqual: testaa, toimiiko funktio oikein.
        """

        self.assertEqual(self.seq.dotplot(DOTPLOTDATA_FILENAME), True)
