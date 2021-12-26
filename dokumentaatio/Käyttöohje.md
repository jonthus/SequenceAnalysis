## DNA Sekvenssianalyysi

Työn tarkoitus on analysoida ja laskea käyttäjän antamia DNA-sekvenssejä ja näyttää tiedot graafisesti, tekstinä tai taulukkomuodossa. Sovelluksella on eri toiminnallisuuksia, joista käyttäjä saa valita.
Sovelluksen perustoiminnallisuudessa kuvataan näitä työkaluja.

### Dokumentaatio
[Määrittelydokumentti](/dokumentaatio/Määrittelydokumentti.md)  
[Tuntikirjanpito](/dokumentaatio/Tuntikirjanpito.md)  
[Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)  
[Latest Release](https://github.com/jonthus/ot-harjoitustyo/releases/tag/viikko6)  


### Asennus
- (pip3 install poetry, jos ei asennettu)
- poetry install
- poetry shell

### Ohjelman suoritus

Ohjelman käynnistäminen
- poetry shell (jos ei aikaisemmin käynnistetty)
- Varmista että olet SequenceAnalysis-kansiossa!
- poetry run invoke start

Ohjelman käyttöohje
- Avaa ohjelmasta haluamasi toiminto ja valitse esimerkkitiedosto kansiosta `input_files`.
- Jos haluat käyttää omaa tiedostoa, niin sen täytyy olla `.txt`-tiedosto FASTA-formaatissa, ja siinä täytyy olla monta DNA-sekvenssiä peräkkäin.
- Ohjelma prosessoi antamasi tiedoston ja näyttää tulokset käyttöliittymässä.
- Ohjelma tallentaa myös taulukot .png-muodossa `output_files` -kansioon.

Testien suoritus
- poetry run invoke test
- poetry run invoke coverage-report
- poetry run invoke lint
