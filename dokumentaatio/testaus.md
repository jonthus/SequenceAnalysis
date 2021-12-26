# Testausdokumentti

## Yksikkötestaus

### Sovelluslogiikka

Testaus tapahtuu suurilta osin `dotplot_service`, `gc_service`, `histogram_service` ja `validation_service` tiedostojen avulla. Testiluokkaan tuodaan nämä, sekä `entities`
-kansion sovelluslogiikan tiedostot, ja ne ajetaan läpi esimerkkisekvenssien kanssa. `validation_service`lle on lisäksi omat testinsä.
Esimerkkisekvensseissä on käytetty ihmisestä löytyvän proteiinin sekvenssiä, sekä kasvin sekvenssiä.
  
`Matplotlib` -kirjaston testaaminen osoittautui tässä projektissa astetta hankalammaksi, niin sen testaaminen hoituu `matplotlib` -kirjaston `compare_images` -työkalulla kirjaston
testidokumentaation mukaisesti. Testi ei välttämättä ole kovin mielekäs, sillä sen käyttämät tiedostot on pregeneroituja, eli kyseessä on ehkä enemmänkin laadullinen testi.
Kuitenkaan en tähän projektiin parempaa ratkaisua keksinyt. Unittestin ja matplotlibin yhteiskäytöstä en löytänyt paljonkaan referenssitapauksia.

Sovelluksen käyttämiseen kuuluu myös läheisesti testitiedostojen käyttäminen, ja nämä on `input_files` -kansiossa. Esimerkkitiedostoina on hiiren genomista, ja kasvin genomista
valitut esimerkkitiedostot. Omia tiedostoja on myös mahdollista käyttää, kunhan ne on `.txt`-päätteisia, ja FASTA-formaatissa, sekä tiedostossa on monta eri sekvenssiä verrattavaksi.

### Testikattavuus

Testikattavuuden haarautumakattavuus on 100%. Testikattavuuteen ei ole otettu mukaan kansion `tests`, eikä kansion `UI` tiedostoja.

![kuva](/dokumentaatio/coverage_loppupalautus.png)

## Järjestelmätestaus

Sovellus on testattu Linux-ympäristössä asentamalla se HY:n etätyöpöydälle, asentamalla se, ja ajamalla kaikki mahdolliset komennot. 
Kaikki määrittelydokumentin listaamat toiminnallisuudet on käyty läpi.
