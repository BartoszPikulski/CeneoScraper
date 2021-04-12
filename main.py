import json
import requests
from bs4 import BeautifulSoup

extracted_opinions = []

product_id = input("Podaj kod produktu: ")
next_page = "https://www.ceneo.pl/{}#tab=reviews".format(product_id)

while next_page:

    response = requests.get(next_page)

    page_dom = BeautifulSoup(response.text, 'html.parser')


    opinions = page_dom.select("div.js_product-review")

    for opinion in opinions:

        opinion_id = opinion["data-entry-id"]
        author = opinion.select("span.user-post__author-name").pop(0).get_text().strip()

        try:
            recomendation = opinion.select("span.user-post__author-recomendation > em").pop(0).get_text().strip()
            recomendation = recomendation=="Polecam"
        except IndexError:
            recomendation = None

        stars = opinion.select("span.user-post__score-count").pop(0).get_text().strip()
        stars = float(stars.split('/')[0].replace(",","."))


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

        submit_date = opinion.select("span.user-post__published > time:nth-of-type(1)").pop(0)['datetime'].strip()

        try:  
            purchase_date = opinion.select("span.user-post__published > time:nth-of-type(2)").pop(0)['datetime'].strip()
            
        except IndexError:
            purchase_date = None

        useful = opinion.select("span[id^=\"votes-yes\"]").pop(0).get_text().strip()
        useless = opinion.select("span[id^=\"votes-no\"]").pop(0).get_text().strip()



        opinion_elements = {
            "opinion_id": opinion_id,
            "author": author,
            "recomendation": recomendation,
            "stars": stars,
            "content": content,
            "cons": cons,
            "pros": pros,
            "purchased": purchased,
            "submit_date": submit_date,
            "purchase_date": purchase_date,
            "useful" : useful,
            "useless" : useless
        }

        extracted_opinions.append(opinion_elements)

    try:
        next_page = "https://ceneo.pl" + page_dom.select("a.pagination__next").pop()["href"]
    except IndexError:
        next_page = None
    
    print(next_page)

with open(f"./opinions/{product_id}.json", 'w', encoding="UTF-8") as fp:
    json.dump(extracted_opinions, fp, indent=4, ensure_ascii=False)

