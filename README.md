# OhTe-Videopokeri

Klassinen videopokeri-peli Pythonilla luotuna. Sovelluksessa pääsee kokemaan klassista videopokeria, joka on tuttua vanhoista (ja uusista) peliautomaateista. Peliä pelataan 1-5 krediitin panoksilla. Tuttuun tapaan pelissä on myös tuplausmahdollisuus, kaikki tai ei mitään!

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.9.0`. Etenenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Dokumentaatio

- Käyttöohje
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuurikuvaus.md)
- Testausdokumentti
- [Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)

## Asennus

Luo hakemisto mihin haluat asentaa sovelluksen, ja mene siihen komentokehotteessa.

Kloonaa repositio hakemistoon komennolla:

```
git clone https://github.com/k0psutin/ohte-2020/
```

Varmista että `pipenv` on asennettuna.

```
python -m pipenv --version
pipenv, version 2020.8.13
```

Asenna virtuaaliympäristön riippuvaisuudet komennolla:

```
python -m pipenv install
```

## Komentorivitoiminnot

### Sovelluksen suorittaminen

Sovellus suoritetaan komennolla

```
python -m pipenv run start
```

### Testaus

Testien ajaminen suoritetaan komennolla

```
python -m pipenv run test
```

### Testikattavuus

Testikattavuus kerätään komennolla:

```
python -m pipenv run coverage
```

Raportti generoituu tämän jälkeen komennolla:

```
python -m pipenv run coverage-report
```

### Pylint

Tiedosto [.pylintrc](.pylintrc) määrittämät tarkistukset voidaan suorittaa komennolla:

```
python -m pipenv run lint
```

---

### Viimeisin julkaisu

[Julkaisu v1.0](https://github.com/k0psutin/ohte-2020/releases/tag/v1.0)
