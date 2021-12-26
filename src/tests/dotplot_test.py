import unittest
import os
import sys
import matplotlib.testing.compare as plt
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services import dotplot_service


COMPARISON_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/testsequence.png')
DOTPLOTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/sequence.png')
TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/dotplotdata.txt')


class TestDotplot(unittest.TestCase):

    def test_histogramService(self):
        """
        Generoi histogrammin.
        Args:

        Returns:

        """
        dotplot_service.dotplot_run(TESTDATA_FILENAME)

    def test_dotplot(self):
        """
        Testaa Sequence-luokan dotplot-funktion toimivuutta vertaamalla sequence.png ja
        testsequence.png tiedostojen samankaltaisuutta.
        Tiedostot ovat generoitu samalla datalla.
        Testi on nyt strukturoitu tällä tavalla, koska matplotlib-kirjaston luomien taulukoiden testaaminen
        on tehty todella monimutkaiseksi.

        Args:
            None

        Returns:
             assertEqual: testaa, toimiiko funktio oikein.
        """

        img1 = DOTPLOTDATA_FILENAME  # actual data
        img2 = COMPARISON_FILENAME  # testidata
        res = plt.compare_images(img1, img2, 0.001)  # palauttaa None jos ei eroavaisuuksia
        self.assertEqual(res, None)