import unittest
from sequence import Sequence
import os

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testitiedosto.txt')

class TestSequence(unittest.TestCase):

    def setUp(self):
        seq = Sequence()
        self.testdata = seq.parse(TESTDATA_FILENAME)

    def test_parse(self):
        """
        Testaa Sequence-luokan parse-funktion toimivuutta testitiedostolla.
        Args:
            None
        Returns:
            assertEqual: vertaa merkkijonoja, palauttaa True jos samat.
        """
        self.assertEqual(self.testdata, "this file has content")