# OhTe-Videopokeri

Klassinen videopokeri-peli Pythonilla luotuna. Sovelluksessa pääsee kokemaan klassista videopokeria, joka on tuttua vanhoista (ja uusista) peliautomaateista. Peliä pelataan 1-5 krediitin panoksilla. Tuttuun tapaan pelissä on myös tuplausmahdollisuus, kaikki tai ei mitään!

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.9.0`. Etenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuurikuvaus.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md)
- [Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)

## Asennus

Luo hakemisto mihin haluat asentaa sovelluksen, ja mene siihen komentokehotteessa.

Kloonaa repositio hakemistoon komennolla:

```bash
git clone https://github.com/k0psutin/ohte-2020/
```

Tai hae uusin [julkaisu](https://github.com/k0psutin/ohte-2020/releases/) ja pura paketti haluamaasi hakemistoon.

Varmista että `pipenv` on asennettuna.

```bash
python -m pipenv --version
pipenv, version 2020.8.13
```

Mene sovelluksen hakemistoon ja asenna virtuaaliympäristön riippuvaisuudet komennolla:

```bash
python -m pipenv install
```

### Sovelluksen poistaminen

Poista asennetut riippuvaisuudet suorittamalla seuraava komento sovelluksen hakemistossa:

```bash
python -m pipenv --rm
```

Sovelluksen hakemiston voi nyt poistaa.

## Komentorivitoiminnot

Huom. Riippuen käyttöjärjestelmästä, komennot suoritetaan joko `python` tai `python3`.

### Sovelluksen suorittaminen

Sovellus suoritetaan komennolla

```bash
python -m pipenv run start
```

Huom! Riippuvaisuudet tulee olla asennettuna ennen käynnistämistä.

### Testaus

Testien ajaminen suoritetaan komennolla

```bash
python -m pipenv run test
```

### Testikattavuus

Testikattavuus kerätään komennolla:

```bash
python -m pipenv run coverage
```

Raportti generoituu tämän jälkeen komennolla:

```bash
python -m pipenv run coverage-report
```

Tämän jälkeen sovelluksen juureen ilmestyy hakemisto `htmlcov` joka sisältää raportin. Raporttia pääsee lukemaan avaamalla kansiossa olevan tiedoston `index.html`.

### Pylint

Sovelluksen koodissa käytetään Google Python [tyylimääräyksiä](https://google.github.io/styleguide/pyguide.html).

Tiedosto [.pylintrc](.pylintrc) määrittämät tarkistukset voidaan suorittaa komennolla:

```bash
python -m pipenv run lint
```

---

### Viimeisin julkaisu

[Julkaisu v2.1](https://github.com/k0psutin/ohte-2020/releases/tag/v2.1)
