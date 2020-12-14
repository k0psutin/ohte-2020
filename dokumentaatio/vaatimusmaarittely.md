# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on luoda viihdyttävä yksinpeli jonka pariin jaksaisi tulla yhä uudestaan ja uudestaan.

## Käyttäjät

Käyttäjiä on vain yksi, eli perustoiminnot omaava pelaaja.

## Käyttöliittymäluonnos

![kayttoliittymaluonnos.png](kuvat/kayttoliittymaluonnos.png)

## Perustoiminnot

- Alkuvalikko

  - Pelaaja voi luoda uuden pelin &#10004;
  - Pelaaja voi jatkaa vanhaa peliä &#10004;
  - Pelaaja voi nähdä tulostaulukon &#10004;
  - Pelaaja voi sulkea sovelluksen &#10004;

- Uusi peli / vanhan jatkaminen

  - Avaa pelinäkymän &#10004;
  - Jos uusi peli, pelaaja aloittaa 10 krediitillä. &#10004;
  - Jos jatketaan vanhaa, haetaan tallennetut krediitit. &#10004;

- Pelinäkymä

  - Pelaaja voi valita panoksen ennen jakoa +/- painikkeilla. &#10004;
  - Pelaaja ei voi vaihtaa panosta kesken jaon. &#10004;
  - Pelaaja voi lukita yhden tai useamman kortin minkä haluaa säilyttää pelipöydällä. &#10004;
  - Jaon aikana, jakamisnapista saadaan vaihtokortit, mikäli kortteja ei ole lukittu. &#10004;
  - Korttien tietyt kombinaatiot antavat voittoja &#10004;
  - Pelaaja voi klikata voittotaulukon auki voittotaulukko-painikkeesta. &#10004;
  - Pelaaja voi lisätä tai vähentää pelattavaa panosta ennen jakamista. &#10004;
  - Pelaaja voi yrittää tuplata halutessaan voittamansa summan &#10004;
    - Tuplaamisessa on mahdollista kaksinkertaistaa voittosumma, mikäli pelaaja arvaa oikein, onko käännetty kortti arvoltaan 1-7 (LOW) vai 8-13 (HIGH). Väärin arvattaessa pelaaja menettää koko summan.
    - Tuplaamista voidaan jatkaa niin kauan kuin halutaan.

- Tulostaulukko
  - Pitää sisällään tilastoja mm. paljonko on ollut enimmillään rahaa, pisin tuplausputki ja kaikkien voittojen summan. &#10004;
  - Pelin loputtua, jos pelaajan tulos on kelvollinen tulostaulukkoon, voidaan tulos tallentaa tulostaulukkoon kolmella kirjaimella. &#10004;

## Jatkokehitysideoita

Perustoimintojen jälkeen voidaan lisätä muitakin korttipelejä kuten mm. ventti (_eng. Blackjack_).
