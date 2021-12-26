import unittest
import os
import sys
import matplotlib.testing.compare as plt
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services import histogram_service

COMPARISON_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/testhistogram.png')
HISTODATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/histogram.png')
TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/histodata.txt')


class TestHistogram(unittest.TestCase):

    def test_histogramService(self):
        """
        Generoi histogrammin.
        Args:
            None
        Returns:
            None
        """
        histogram_service.histogram_run(TESTDATA_FILENAME)

    def test_histogram(self):
        """
        Testaa Histogram-luokan histogrammin generoinnin toimivuutta vertaamalla histogram.png ja
        testhistogram.png tiedostojen samankaltaisuutta.
        Tiedostot ovat generoitu samalla datalla.
        Testi on nyt strukturoitu tällä tavalla, koska matplotlib-kirjaston luomien taulukoiden testaaminen
        on tehty todella monimutkaiseksi.

        Args:
            None

        Returns:
             assertEqual: testaa, toimiiko funktio oikein.
        """

        img1 = HISTODATA_FILENAME  # actual data
        img2 = COMPARISON_FILENAME  # testidata
        res = plt.compare_images(img1, img2, 0.001)  # palauttaa None jos ei eroavaisuuksia
        self.assertEqual(res, None)