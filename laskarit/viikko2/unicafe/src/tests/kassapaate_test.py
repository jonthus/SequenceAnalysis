import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(100000)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')

    def test_kateisosto_edullinen_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100240')
        self.assertEqual(str(self.kassapaate.edulliset), '1')

    def test_kateisosto_edullinen_eiriittava(self):
        self.kassapaate.syo_edullisesti_kateisella(50)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '0')

    def test_kateisosto_maukas_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100400')
        self.assertEqual(str(self.kassapaate.maukkaat), '1')

    def test_kateisosto_maukas_eiriittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    #Maksukorttitestit

    def test_korttiosto_edullinen_riittava(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti.saldo), '99760')
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '1')

    def test_korttiosto_edullinen_eiriittava(self):
        self.kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti.saldo), '10')
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '0')

    def test_korttiosto_maukas_riittava(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti.saldo), '99600')
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.maukkaat), '1')

    def test_korttiosto_maukas_eiriittava(self):
        self.kortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti.saldo), '10')
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_kortin_lataaminen(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(str(self.kortti.saldo), '100500')
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100500')

    def test_kortin_lataaminen_epaonnistuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -50)
        self.assertEqual(str(self.kortti.saldo), '100000')
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')