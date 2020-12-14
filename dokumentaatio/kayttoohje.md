# Käyttöohje

Lataa projektin viimeisimmän [releases](https://github.com/k0psutin/ohte-2020/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

Sovellus luo automaattisesti tallennustiedostot. Tulostaulukon alustaminen tapahtuu siis poistamalla `highscores.dat` -tiedosto.

## Ohjelman käynnistäminen

Huom. Riippuen käyttöjärjestelmästä, komennot suoritetaan joko `python` tai `python3`.

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

`python -m pipenv install`

Nyt ohjelman voi käynnistää komennolla:

`python -m pipenv run start`

### Uuden pelin aloittaminen

Sovellus käynnistyy päävalikkoon:

![paavalikko.png](kuvat/paavalikko.png)

`New game`-painikkeesta aloitetaan uusi peli. Ohjelma varoittaa käyttäjää jos löytyy aktiivinen pelitallennus. Muuten peli siirtyy suoraan `pelinäkymään`.

![varoitus.png](kuvat/varoitus.png)

`No`-painikkeella palataan takaisin alkuvalikkoon, ja tällöin vanhaa tallennusta voidaan jatkaa `Continue`-painikkeella.

Jos siitä huolimatta haluaa aloittaa uuden pelin, tällöin jatketaan tapahtumaa `Yes`-painikkeella.

Peli tallentaa pelitilanteen automaattisesti kun poistut pelinäkymästä päävalikkoon.

### Pelinäkymä

![pelinakyma.png](kuvat/pelinakyma.png)

Vasemmasta alareunasta näet jatkuvasti krediittien tilanteen. Kun krediitit laskevat nollaan, on peli hävitty.

![krediitit.png](kuvat/krediitit.png)

Ennen pelivuoroa asetetaan pelissä käytettävä panos, `+/-`-painikkeista. Kun pelivuoro on käynnissä, panosta ei voida muuttaa.

![panos.png](kuvat/panos.png)

Panos vaikuttaa voittojen suuruuteen. Mitä suurempi panos, sitä enemmän voit voittaa. `Payouts`-painikkeella avataan maksutaulukko, mistä voi nähdä että kuinka paljon milläkin panoksella on mahdollista voittaa.

![voittotaulukko.png](kuvat/voittotaulukko.png)

Kun panos on asetettu, pelivuoro aloitetaan `Deal`-painikkeella.

![jakopainike.png](kuvat/jakopainike.png)

### Yhden vuoron pelaaminen

![pelivuoro.png](kuvat/pelivuoro.png)

Pelivuoron alettua, pelipöydälle jaetaan viisi korttia, mistä valitaan mieleiset. Valitseminen tapahtuu kunkin kortin alapuolella olevalla `Hold`-painikkeella, joka lukitsee kortin - eli sitä ei vaihdeta korttienvaihdon yhteydessä.

![korttienpito.png](kuvat/korttienpito.png)

Kun mielekkäät kortit on valittuna, vaihdetaan ei-lukitut kortit uusiin jatkamalla pelivuoroa `Deal`-painikkeesta.

![voitto.png](kuvat/voitto.png)

Kun uudet kortit on jaettu, ja pelaajalla on voittava käsi, ilmoitetaan siitä voittoilmoituksella. Voittorahat voidaan ottaa talteen, tai kokeilla kaksinkertaistaa `voiton tuplaamisella`.

### Voiton tuplaaminen

![tuplausnakyma.png](kuvat/tuplausnakyma.png)

Voittosumma on mahdollista kaksinkertaistaa arvaamalla onko seuraavan kortin arvo 7 tai alle `low` vai yli 7 `high`.

Tämä tapahtuu painikkeista `Low` ja `High`.

Tuplaamista voi jatkaa niin kauan, kuin oma kantti kestää. Väärin arvattaessa menetetään kaikki jo tähänasti kerätyt krediitit.
