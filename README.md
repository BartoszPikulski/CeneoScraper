# CeneoScraper

## Etap 1
### 1. Analiza stuktury opinii w serwisie [Ceneo.pl]

|Składowa|Selekto CSS|Nazwa zmiennej|Typ danych|
|--------|-----------|--------------|----------|
|Opinia|div.js_product-review|opinion||
|Id opinii|data-entry-id|opinion_id||
|Autor|span.user-post__author-name|author||
|Rekomendacja|span.use-post__author-recomendation > em|recomendation||
|Liczba gwiazdek|span.user-post__score-count|stars||
|Treść opinii|div.user-post__text|content||
|Lista wad|div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item|pros||
|Lista zalet|div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item|cons||
|Potwierdzenie zakupem|div.review-pz|purchased||
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|submit_date||
|Data zakupu produktu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date||
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful||
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless||


### 2. Pobranie składowych pojedynczej opinii
- pobranie kodu pojedynczej stony z opiniami
- wyodębnienie z kodu strony kodu pojedynczej opinii
- pobranie do pojedynczych zmiennych poszczegolnych skladowych na podstawie selektorów