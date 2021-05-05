from os import listdir
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)

print(*listdir("opinions"), sep="\n")

product_id = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

average_score = opinions.stars.mean()
opinions_count = opinions.shape[0]

pros_count = opinions.pros.astype(bool).sum()
cons_count = opinions.cons.astype(bool).sum()
print(f""" O produkcie dostepnych jest {opinions_count} opinii.
Dla {pros_count} opinii podana zostala lista zalet, a dla {cons_count} lista wad.
Średnia ocena produktu wyznaczona na podstawie liczby gwiazdek wynosi {average_score}.
""")

stars_count = opinions.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value = 0)
stars_count.plot.bar()
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.title("Czestosc wystepowania poszczegolnych ocen produktu")
plt.savefig(f"./figures/{product_id}_stars.png")
plt.close()


recommendations = opinions.recommendation.value_counts(dropna = False).reindex([True, False, float("Nan")], fill_value = 0)
recommendations.plot.pie(
    label = "",
    labels = ['Polecam', 'Nie mam zdania', 'Nie polecam'],
    colors = ['forestgreen', 'crimson', 'yellow'],
    autopct = "%1.1f%%",
    pctdistance = 1.1,
    labeldistance = 1.4
)
plt.title("udzial poszczegolnych rekomendacji w opiniach")
plt.legend(bbox_to_anchor = (1.0, 1.0))
plt.tight_layout()
plt.savefig(f"./figures/{product_id}_rcmd.png", bbox_inch = "tight")
plt.close()
# opinions.pros = opinions.pros.replace(list(), None)
# pros_count = opinions.pros.notnull().count()
# rows_count = opinions.shape[0]

# print(rows_count,"=>",pros_count)
# print(opinions)