## Käyttöohje

### Ohjelman toiminnot

Ohjelman on neljä eri näkymää ja kolme eri toimintoa:  
- Etusivu  
  - Kahden sekvenssin samanlaisuus  
  - Sekvenssin GC-% laskeminen  
  - Sekvenssien pituuksien vertailu  

Tässä dokumentissa esitellään ensimmäisen toiminnon käyttö esimerkkinä. Muiden toimintojen käyttö on lähes identtistä.

### Ohjelman käynnistäminen
```
- poetry install
- Varmista että olet pääkansiossa!
- poetry run invoke start
```

### Esimerkki 

Kun avaat sovelluksen, näät alla olevan etusivunäkymän.

![kuva](/dokumentaatio/Käyttöohje_kuvat/etusivu.png)

Avataan esimerkiksi ensimmäinen toiminto, Kahden sekvenssin vertailu. Avautuu seuraavanlainen näkymä.
Kun painetaan nappia "Valitse tiedosto", niin avautuu tiedostonvalitsija. 

![kuva](/dokumentaatio/Käyttöohje_kuvat/vertailu.png)

Alla olevassa kuvassa on näytetty esimerkkitiedostojen sijainti.

![kuva](/dokumentaatio/Käyttöohje_kuvat/filepath.png)

Kun tiedosto valitaan, ohjelma prosessoi hetken verran ja sen jälkeen näyttää datasta prosessoidun tiedon taulukkona.

![kuva](/dokumentaatio/Käyttöohje_kuvat/esimerkki.png)
