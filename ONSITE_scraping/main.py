from pprint import pprint
import json

import requests
from bs4 import BeautifulSoup




# filtruj jidlo z radku
def filtruj_jidlo_ze_dne(li_tag) -> dict:
    radky = li_tag.get_text('\n').splitlines()
    # print(radky)
    # radky = [r.replace('\xa0', ' ') for r in radky]
    # print(radky)
    # print(jidlo_a_cena(radky[1]))
    return {
        'den': radky[0],
        'polevka': jidlo_a_cena(radky[1]),
        'menu_1': jidlo_a_cena(radky[2]),
        'menu_2': jidlo_a_cena(radky[3]),
        'menu_3': jidlo_a_cena(radky[4]),
        'menu_4': jidlo_a_cena(radky[5])
    }

def jidlo_a_cena(radky: str) -> dict:
    *jidlo, cena = radky.split(' ')
    # print(jidlo, cena)
    return {' '.join(jidlo): int(cena[:-2])}


# json vystup
# nazev dne, menu_1, nazev jidla: cena


# oddelit jidlo a cenu

# ulozit menu do json souboru


def main():
    # zpracuj odpoved serveru
    url = "https://www.taste-of-india.cz/"
    odpoved = requests.get(url)
    # print(odpoved.text)

    soup = BeautifulSoup(odpoved.text, 'html.parser')

    # print(soup.find('ul', {'class': 'daily-menu'}).prettify())

    # najdi sekci menu a v ni jednotlive dny
    sekce_menu = soup.find('ul', {'class': 'daily-menu'})
    dny_menu = sekce_menu.find_all('li')
    # projdeme cely tyden
    menu_slovnik = {}
    for den in dny_menu[1:6]:
        denni_nabidka = filtruj_jidlo_ze_dne(den)
        nazev_dne = denni_nabidka.pop('den')
        menu_slovnik[nazev_dne] = denni_nabidka
    pprint(menu_slovnik)
    uloz_menu_do_json(menu_slovnik, 'prvni_pokus.json')

def uloz_menu_do_json(menu_slovnik, nazev_souboru: str):
    with open(nazev_souboru, "w", encoding="utf-8") as json_soubor:
        json.dump(menu_slovnik, json_soubor)
    pprint(f'Menu ulozeno do souboru {nazev_souboru}')



if __name__ == '__main__':
    main()