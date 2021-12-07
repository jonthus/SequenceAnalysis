## OT-harjoitustyö  

### Dokumentaatio
[Määrittelydokumentti](/dokumentaatio/Määrittelydokumentti.md)  
[Tuntikirjanpito](/dokumentaatio/Tuntikirjanpito.md)


### Asennus
- (pip3 install poetry, jos ei asennettu)
- poetry install
- pip3 install -r requirements.txt

### Ohjelman suoritus

Ohjelman käynnistäminen
- poetry shell
- poetry run invoke start

Testien suoritus
- poetry run invoke test
- poetry run invoke coverage-report
- poetry run invoke lint
