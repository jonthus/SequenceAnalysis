## Vaatimusmäärittely

### Sovelluksen tarkoitus  
Sovelluksen tarkoitus on analysoida käyttäjän antamia DNA-sekvenssejä ja näyttää tiedot graafisesti, tai taulukkomuodossa. Sovelluksella on eri toiminnallisuuksia, joista käyttäjä saa valita.
Sovelluksen perustoiminnallisuudessa kuvataan näitä työkaluja.
  
### Käyttöliittymäluonnos
Käyttöliittymässä ei ole kirjautumista, sovelluksen käynnistäminen riittää.
Käyttäjä aloittaa valitsemalla haluamansa työkalun.
Käyttäjä valitsee nukleotidisekvenssit valitsemalla haluamansa tiedostot, jotka ovat FASTA- tai FASTQ-formaatissa.
Sovellukseen on mahdollista lisätä sekvenssejä käytettäväksi (sqlite).
Käyttäjä voi valita halutun määrän sekvenssejä analysoitavaksi riippuen työkalusta.
Käyttäjä ajaa työkalun, ja saa siitä tulokset, jotka ovat tallennettavissa.

### Perusversion tarjoama toiminnallisuus
Sovelluksen perustoiminnallisuuteen kuuluu erilaisia työkaluja.

1. Kahden (tai enemmän) nukleotidisekvenssin vertailua. DNA-sekvenssit ovat FASTA- tai FASTQ-formaatissa. Näistä sekvensseistä tulostuu näytölle Scatter Plot -taulukko, 
jossa näytetään niiden samankaltaisuus prosentuaalisesti. Tämä on toteutettu Viikkopalautuksessa 4.
2. Ketjujen nukleotidimäärien esittäminen taulukkomuodossa (GC-pitoisuus).
3. Ketjujen pituuksien vertailua histogrammina.

Saadut taulukot on mahdollista tallentaa käyttäjän haluamassa formaatissa.

### Jatkokehitysideoita
Sovellukseen on ajankäytön mukaisesti mahdollista tehdä jatkotoiminnallisuuksia.
Näitä ovat esimerkiksi:
- Multiple Sequence Alignment
- DNA sekvenssin translaatio ja transkriptio DNA -> RNA -> Proteiini.
- Sekvenssien siivoaja (jos on paljon tuntemattomia nukleotideja).

