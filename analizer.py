from os import listdir
import pandas as pd

pd.set_option('display.max_columns', None)

#print(*listdir("opinions"), sep="\n")

product_id = input("Podaj kod produktu: ")

opinions = pd.read_json(f"C:/Users/Drive/Python/Python UEK/CP2/CeneoScraper/opinions/{product_id}.json")

average_score = opinions.stars.mean()

stats_count = opinions.groupby('stars').count()

print(opinions.info())
print(sum(1 for x in opinions.pros if x))