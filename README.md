# Gallery

Yksinkertainen galleria kuvien julkaisemiseen/jakamiseen.

Kuka tahansa rekisteröitynyt käyttäjä voi kuvien julkaisemisen lisäksi myös 
luoda tililleen kuvakokoelmia, ja lisätä, sekä poistaa, niihin vapaasti omia 
tai muiden julkaisemia kuvia. Jokaisella kuvakokoelmalla tulee olla nimi ja 
ainakin yksi avainsana, joka kuvaa sen sisältöä. Mikäli kuvan alkuperäinen 
julkaisija poistaa kyseisen, se poistuu myös kaikista niistä kokoelmista, 
missä se on.

Kuvan julkaisuun sisältyy kuvan itsensä lisäksi:
  * Nimi.
  * Julkaisu päivämäärä.
  * Julkaisijan nimi.
  * Joukko avainsanoja.
  * Kommenttiosio.

Kuka tahansa käyttäjä voi selailla kuvia vapaasti ja hakea kuvia avaisanojen, 
julkaisijoiden ja kokoelmien avulla. Vain rekisteröityneet käyttäjät voi 
kommentoida julkaisuja.

## Kokeilu/testaus:


```console 
python3 -m venv venv
```
```console 
source venv/bin/activation
```
```console 
pip install flask
```
```console 
pip install exifread
```
```console 
flask run
```

