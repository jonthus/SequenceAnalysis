import unittest
from maksukortti import Maksukortti

"""
    Kortin saldo alussa oikein
    Rahan lataaminen kasvattaa saldoa oikein
    Rahan ottaminen toimii
        Saldo vähenee oikein, jos rahaa on tarpeeksi
        Saldo ei muutu, jos rahaa ei ole tarpeeksi
        Metodi palauttaa True, jos rahat riittivät ja muuten False
"""

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortin_lataaminen(self):
        self.maksukortti.lataa_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 0.6")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
        return True

    def test_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        return False

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

