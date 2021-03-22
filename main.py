import requests

response = requests.get("https://www.ceneo.pl/96797516#tab=reviews")
print(response.text)