# CeneoScraper

## Etap 1
### 1. Analiza stuktury opinii w serwisie [Ceneo.pl]

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|-----------|--------------|----------|
|Opinia|div.js_product-review|opinion|object|
|Id opinii|data-entry-id|opinion_id|str|
|Autor|span.user-post__author-name|author|str|
|Rekomendacja|span.use-post__author-recomendation > em|recomendation|bool|
|Liczba gwiazdek|span.user-post__score-count|stars|float|
|Treść opinii|div.user-post__text|content|str|
|Lista wad|div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item|cons|list|
|Lista zalet|div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item|pros|list|
|Potwierdzenie zakupem|div.review-pz|purchased|bool|
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|submit_date|str|
|Data zakupu produktu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|str|
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful|int|
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless|int|


### 2. Pobranie składowych pojedynczej opinii
- pobranie kodu pojedynczej stony z opiniami
- wyodębnienie z kodu strony kodu pojedynczej opinii
- pobranie do pojedynczych zmiennych poszczegolnych skladowych na podstawie selektorów
- obsługa błędów
- dobranie typów danych do wartości zmiennych

### Etap 2 Ekstrakcja wszystkich opinii o produkcie z pojedynczej strony
- zapis składowych pojedynczej opinii do słownika
- zdefiniowanie listy do przechowywania wszystkich opinii o danym produkcie
- dodanie pętli, która wykonuje operację esktrakcji dla wszystkich opinii pobrancyh z pojedynczej strony


### Etap 3 Ekstrakcja wszystkich opinii o produkcie z wszystkich stron
- dodanie pętli, która pobiera i anlizuje kolejne strony z opiniami o produkcie
- dodanie możliwości podania kodu produktu "z klawiatury"
- dodanie zapisu wszystkich opinii o produkcie do pliku json

### Etap 4 Refactoring
- 