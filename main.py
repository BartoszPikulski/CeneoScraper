import json
import requests
from bs4 import BeautifulSoup

def extract_element(opinion, selector, attribute=None):
    try:
        if attribute:
            if isinstance(attribute, str):
                return opinion.select(selector).pop(0)[attribute].strip()
            else:
                return [x.get_text().strip() for x in opinion.select(selector)]
        else:
            return opinion.select(selector).pop(0).get_text().strip()
    except IndexError:
        return None

selectors = {
            "opinion_id": ["data-entry-id"],
            "author": ["span.user-post__author-name"],
            "recommendation": ["span.user-post__author-recomendation > em"],
            "stars": ["span.user-post__score-count"],
            "content": ["div.user-post__text"],
            "cons": ["div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item"],
            "pros": ["div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item"],
            "purchased": ["span.user-post__published > time:nth-of-type(2)"],
            "submit_date": ["span.user-post__published > time:nth-of-type(1)", "datetime"],
            "purchase_date": ["span.user-post__published > time:nth-of-type(2)", "datetime"],
            "useful" : ["span[id^=\"votes-yes\"]"],
            "useless" : ["span[id^=\"votes-no\"]"]
        }

extracted_opinions = []

product_id = input("Podaj kod produktu: ")
next_page = "https://www.ceneo.pl/{}#tab=reviews".format(product_id)

while next_page:

    response = requests.get(next_page)
    page_dom = BeautifulSoup(response.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")

    for opinion in opinions:

        opinion_elements = {key:extract_element(opinion, *args)
                            for key, args in selectors.items()}

        opinion_elements["opinion_id"] = opinion["data-entry-id"]
        opinion_elements['useful'] = int(opinion_elements['useful'])
        opinion_elements['useless'] = int(opinion_elements['useful'])
        opinion_elements['recommendation']= True if  opinion_elements['recommendation']=="Polecam" else False if opinion_elements['recommendation']=='Nie polecam' else  opinion_elements['recommendation']
        stars = float(opinion_elements['stars'].split('/')[0].replace(",","."))

        extracted_opinions.append(opinion_elements)

    try:
        next_page = "https://ceneo.pl" + page_dom.select("a.pagination__next").pop()["href"]
    except IndexError:
        next_page = None
    
    print(next_page)

with open(f"./opinions/{product_id}.json", 'w', encoding="UTF-8") as fp:
    json.dump(extracted_opinions, fp, indent=4, ensure_ascii=False)

