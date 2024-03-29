## DNA Sekvenssianalyysi

Työn tarkoitus on analysoida ja laskea käyttäjän antamia DNA-sekvenssejä ja näyttää tiedot graafisesti, tekstinä tai taulukkomuodossa. Sovelluksella on eri toiminnallisuuksia, joista käyttäjä saa valita.

Sovelluksella on neljä eri näkymää ja kolme eri toimintoa:  
- Etusivu  
  - Kahden sekvenssin samanlaisuus  
  - Sekvenssin GC-% laskeminen  
  - Sekvenssien pituuksien vertailu  

Käyttöohjeessa on annettu esimerkki ohjelman suorittamisesta.

### Dokumentaatio
[Käyttöohje](/dokumentaatio/Käyttöohje.md)  
[Testausdokumentti](/dokumentaatio/testaus.md)  
[Määrittelydokumentti](/dokumentaatio/Määrittelydokumentti.md)  
[Tuntikirjanpito](/dokumentaatio/Tuntikirjanpito.md)  
[Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)  
[Latest Release](https://github.com/jonthus/ot-harjoitustyo/releases/tag/loppupalautus)  


### Asennus
```
- (pip3 install poetry, jos ei asennettu)
- poetry install
```

### Ohjelman suoritus

Ohjelman käynnistäminen
```
- Varmista että olet pääkansiossa!
- poetry run invoke start
```

Ohjelman käyttöohje
- Avaa ohjelmasta haluamasi toiminto ja valitse esimerkkitiedosto kansiosta `input_files`.
- Jos haluat käyttää omaa tiedostoa, niin sen täytyy olla `.txt`-tiedosto FASTA-formaatissa, ja siinä täytyy olla monta DNA-sekvenssiä peräkkäin.
- Ohjelma prosessoi antamasi tiedoston ja näyttää tulokset käyttöliittymässä.
- Ohjelma tallentaa myös taulukot .png-muodossa `output_files` -kansioon.

Testien suoritus
```
- poetry run invoke test
- poetry run invoke coverage-report
- poetry run invoke lint
```
