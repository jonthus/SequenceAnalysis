# DNA Sekvenssianalyysi
Työn tarkoitus on analysoida ja laskea käyttäjän antamia DNA-sekvenssejä ja näyttää tiedot graafisesti, tekstinä tai taulukkomuodossa. Sovelluksella on eri toiminnallisuuksia, joista käyttäjä saa valita.
Sovelluksen perustoiminnallisuudessa kuvataan näitä työkaluja.

## Dokumentaatio
[Käyttöohje](/dokumentaatio/Käyttöohje.md)  
[Määrittelydokumentti](/dokumentaatio/Määrittelydokumentti.md)  
[Tuntikirjanpito](/dokumentaatio/Tuntikirjanpito.md)  
[Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)  
[Latest Release](https://github.com/jonthus/ot-harjoitustyo/releases/tag/viikko6)  

## Asennus
```
- (pip3 install poetry, jos ei asennettu)
- poetry install
- poetry shell
```
## Ohjelman suoritus

### Ohjelman käynnistäminen
```
- poetry shell (jos ei aikaisemmin käynnistetty)
- Varmista että olet src-kansiossa!
- poetry run invoke start
```

### Ohjelman käyttöohje

- Avaa haluamasi toiminto ja valitse tiedosto (oma tiedosto FASTA-formaatissa, tai tiedosto kansiosta src/files).
- Ohjelma prosessoi antamasi tiedoston ja näyttää tulokset käyttöliittymässä.

### Testien suoritus

```
- poetry run invoke test
- poetry run invoke coverage-report
- poetry run invoke lint
```
