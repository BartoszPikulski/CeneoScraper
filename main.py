import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ceneo.pl/96796516#tab=reviews")

page_dom = BeautifulSoup(response.text, 'html.parser')

#print(page_dom.prettify())

opinion = page_dom.select("div.js_product-review").pop(0)
opinion_id = opinion["data-entry-id"]
author = opinion.select("span.user-post__author-name").pop(0).get_text().strip()
try:
    recomendation = opinion.select("span.user-post__author-recomendation > em").pop(0).get_text().strip()
    recomendation = recomendation=="Polecam"
except IndexError:
    recomendation = None

stars = opinion.select("span.user-post__score-count").pop(0).get_text().strip()
stars = float(stars.split('/')[0])


content = opinion.select("div.user-post__text").pop(0).get_text().strip()

try:
    cons = opinion.select("div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item")
    cons = [x.get_text().strip() for x in cons]
except IndexError:
    cons = None

try:  
    pros = opinion.select("div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item")
    pros = [x.get_text().strip() for x in pros]
except IndexError:
    pros = None

try:  
    purchased = bool(opinion.select("div.review-pz").pop(0).get_text().strip())
except IndexError:
    purchased = False

submit_date = opinion.select("span.user-post__published > time:nth-child(1)").pop(0)['datetime'].strip()

try:  
    purchase_date = opinion.select("span.user-post__published > time:nth-child(2)").pop(0)['datetime'].strip()
except IndexError:
    purchase_date = None

useful = opinion.select("span[id^=\"votes-yes\"]").pop(0).get_text().strip()
useless = opinion.select("span[id^=\"votes-no\"]").pop(0).get_text().strip()

print(author, recomendation, stars, content, cons, pros, purchased, submit_date, purchase_date,
    useful, useless, sep = '\n')