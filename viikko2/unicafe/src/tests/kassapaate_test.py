import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luodun_kassapaatteen_rahamaara_ja_myydyt_lounaat_on_oikein(self):
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100000, lounaita myyty 0")

    def test_rahamaara_kasvaa_edullisen_lounaan_hinnalla_ja_vaihtorahan_suuruus_on_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100240, lounaita myyty 1")

    def test_kun_maksu_on_riittava_edulliseen_ruokaan_määrä_ja_kassa_kasvaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100240, lounaita myyty 1")

    def test_rahamaara_kasvaa_maukkaan_lounaan_hinnalla_ja_vaihtorahan_suuruus_on_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100400, lounaita myyty 1")

    def test_kun_maksu_on_riittava_maukkaan_ruokaan_määrä_ja_kassa_kasvaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100400, lounaita myyty 1")

    def test_jos_maksu_ei_riita_edulliseen_palautetaan_rahat_ja_kassa_ei_muutu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100000, lounaita myyty 0")

    def test_jos_maksu_ei_riita_makkauseen_palautetaan_rahat_ja_kassa_ei_muutu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100000, lounaita myyty 0")

    def test_jos_kortilla_on_tarpeeksi_rahaa_edulliseen_lounaaseen_palauta_true(self):
        kortti = Maksukortti(240)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))

    def test_jos_kortilla_on_tarpeeksi_rahaa_maukkaaseen_lounaaseen_palauta_true(self):
        kortti = Maksukortti(400)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_jos_kortilla_on_tarpeeksi_rahaa_edulliseen_lounaaseen_myydyt_lounaat_kasvavat_yhdella(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100000, lounaita myyty 1")

    def test_jos_kortilla_on_tarpeeksi_rahaa_maukkaaseen_lounaaseen_myydyt_lounaat_kasvavat_yhdella(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100000, lounaita myyty 1")

    def test_jos_kortin_saldo_ei_riita_edulliseen_lounaaseen_palautetaan_false(self):
        kortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))

    def test_jos_kortin_saldo_ei_riita_maukkaasti_lounaaseen_palautetaan_false(self):
        kortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_jos_kortin_saldo_ei_riita_edulliseen_lounaaseen_palautetaan_myydyt_eivat_nouse(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100000, lounaita myyty 0")

    def test_jos_kortin_saldo_ei_riita_maukkaasti_lounaaseen_palautetaan_myydyt_eivat_nouse(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100000, lounaita myyty 0")

    def test_korttia_ladatessa_kortin_saldo_muuttuu_ja_kassan_rahamaara_kasvaa_ladatulla_summalla(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100500, lounaita myyty 0")

    def test_korttia_ladatessa_negatiivisella_maaralla_ei_kassan_rahamaara_muutu(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(str(self.kassapaate),
                         "rahaa 100000, lounaita myyty 0")
