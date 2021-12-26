## Vaatimusmäärittely

### Sovelluksen tarkoitus  
Sovelluksen tarkoitus on analysoida käyttäjän antamia DNA-sekvenssejä ja näyttää tiedot graafisesti, tai taulukkomuodossa. Sovelluksella on eri toiminnallisuuksia, joista käyttäjä saa valita.
Sovelluksen perustoiminnallisuudessa kuvataan näitä työkaluja.
  
### Käyttöliittymäluonnos
Käyttöliittymässä ei ole kirjautumista, sovelluksen käynnistäminen riittää.
Käyttäjä aloittaa valitsemalla haluamansa työkalun.
Käyttäjä valitsee nukleotidisekvenssit valitsemalla haluamansa tiedostot, jotka ovat FASTA-formaatissa `.txt`-päätteen tiedostona.
Sekvenssejä olisi hyvä olla 2 tai enemmän tiedostossa järkevän analysoinnin takaamiseksi.
Käyttäjä ajaa työkalun, ja saa siitä tulokset, jotka tallennetaan `output_files` -kansioon.

### Perusversion tarjoama toiminnallisuus
Sovelluksen perustoiminnallisuuteen kuuluu erilaisia työkaluja.

1. Kahden (tai enemmän) nukleotidisekvenssin vertailua. DNA-sekvenssit ovat FASTA- tai FASTQ-formaatissa. Näistä sekvensseistä tulostuu näytölle Dotplot -taulukko, 
jossa näytetään niiden samankaltaisuus prosentuaalisesti.
2. Ketjujen nukleotidimäärien esittäminen prosentuaalisesti (GC-pitoisuus).
3. Ketjujen pituuksien vertailua histogrammina.

Saadut taulukot tallennetaan `.png` -formaatissa.

### Jatkokehitysideoita
Sovellukseen on ajankäytön mukaisesti mahdollista tehdä jatkotoiminnallisuuksia.
Näitä ovat esimerkiksi:
- Multiple Sequence Alignment
- DNA sekvenssin translaatio ja transkriptio DNA -> RNA -> Proteiini.
- Sekvenssien siivoaja (jos on paljon tuntemattomia nukleotideja).

