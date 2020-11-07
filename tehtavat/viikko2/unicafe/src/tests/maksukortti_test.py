import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(190)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(10))

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.assertFalse(self.maksukortti.ota_rahaa(15))
