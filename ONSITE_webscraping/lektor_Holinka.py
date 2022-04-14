import csv

from pprint import pprint

import requests
from bs4 import BeautifulSoup

# url = 'https://www.idnes.cz/'
#
# odpoved_serveru = requests.get(url)
#
# rozdelene_html = BeautifulSoup(odpoved_serveru.content, 'html.parser')
# vsechny_elementy_a = rozdelene_html.find_all('a', {'class': 'art-link'})
#
# vysledky = {}
# for elem_a in vsechny_elementy_a:
#     vysledky[elem_a['href']] = elem_a.get_text()
#
# for clanek in vysledky:
#     print(vysledky[clanek].strip())


url = 'https://heroes3.cz/hraci/index.php?page=1&order=&razeni=DESC'

odpoved_serveru = requests.get(url)

# print(type(odpoved_serveru))

# print(type(odpoved_serveru.text))

soup = BeautifulSoup(odpoved_serveru.text, 'html.parser')

# print(type(soup))

# print(soup)
# print(soup.prettify())

table_tag_top = soup.find('table', {'class': 'tab_top'})
# print(table_tag_top.prettify())

vsechny_tr = table_tag_top.find_all('tr')
# print(vsechny_tr[1])

# for tr in vsechny_tr[1:]:
#     td_na_radku = tr.find_all('td')
#     print(td_na_radku[2].get_text())
#     break

def vyber_atributy_z_radku(tr_tag: "import bs4.element"):
    """
    z kaydeho radku (tr) vyber urcite bunky (td)[index]
    a zabal je do slovniku
    """
    return {
        'poradi': tr_tag[0].get_text(),
        'jmeno': tr_tag[2].get_text(),
        'body': tr_tag[3].get_text(),
        'vitezstvi': tr_tag[5].get_text(),
        'cellkem_her': tr_tag[6].get_text(),
        'uspesnost': tr_tag[7].get_text(),
    }

vysledky = []

for tr in vsechny_tr[1:]:
    # td_na_radku = tr.find_all('td')
    # data_hrace = vyber_atributy_z_radku(td_na_radku)
    # vysledky.append(data_hrace)
# anebo kratsi zapis ;-)
    vysledky.append(vyber_atributy_z_radku(tr.find_all('td')))

# pprint(vysledky)

# comprehension:
data_o_hracich = [
    vyber_atributy_z_radku(tr.find_all('td'))
    for tr in vsechny_tr[1:]
]

# pprint(data_o_hracich)


def zapis_data(data: list, jmeno_souboru: str):
    with open(jmeno_souboru, mode='w', encoding='UTF-8', newline='') as csv_output:
        sloupce = data[0].keys()
        zapis = csv.DictWriter(csv_output, fieldnames=sloupce)
        zapis.writeheader()
        zapis.writerows(data)
    print('File written')


zapis_data(data_o_hracich, 'tabulka_1.csv')