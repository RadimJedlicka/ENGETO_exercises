#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def main():
    datum = datetime.now().strftime("%Y%m%d")
    restaurace = "Taste_of_india"
    url = "https://www.taste-of-india.cz/#daily-menu"
    jmeno_souboru = f"{datum}_{restaurace}_menu.json"
    menu_slovnik = denni_menu(url, jmeno_souboru)
    uloz_menu_do_json(menu_slovnik, jmeno_souboru)
    vypis_do_konzole(menu_slovnik, restaurace, oblibene_jidlo='Jalfrezi')


def denni_menu(url: str, jmeno_souboru: str) -> dict:
    """
    Funkce, ktera zajistuje cely proces web scrapingu.
    """
    soup = zpracuj_odpoved_serveru(url)
    vsechny_li = najdi_sekci_menu(soup)
    tento_tyden = [filtruj_jidlo_z_radku(li) for li in vsechny_li[1:6] ]
    # pprint(tento_tyden)
    tento_tyden_slovnik = {den.pop('den'):den for den in tento_tyden}
    # pprint(tento_tyden_slovnik)
    return tento_tyden_slovnik


def zpracuj_odpoved_serveru(url):
    """
    Odesli pozadavek na prislusnou adresu 'url' a vracenou
    odpoved parsuj pomoci 'BeautifulSoup'.
    """
    odpoved = requests.get(url)
    return BeautifulSoup(odpoved.text, 'html.parser')


def najdi_sekci_menu(soup):
    """
    V zadanem objektu 'soup' vyhledej html tagy s dennim menu.

    :return: bs4.element.ResultSet
    """
    # ul = unordered list
    sekce_menu = soup.find("ul", {"class": "daily-menu"})
    return sekce_menu.find_all("li")


def filtruj_jidlo_z_radku(li_tag):
    """
    Z kazdeho radku ('\n') vyber jidlo a jeho cenu
    a zabal je do slovniku

    :return: dict
    """
    radky = li_tag.get_text("\n").splitlines()
    # '&nbsp' = nonbreaking space is parsed as '\xa0'
    radky = [r.replace("\xa0", " ") for r in radky]
    return {
        "den": radky[0],
        "polevka": jidlo_a_cena(radky[1]),
        "menu_1": jidlo_a_cena(radky[2]),
        "menu_2": jidlo_a_cena(radky[3]),
        "menu_3": jidlo_a_cena(radky[4]),
        "menu_4": jidlo_a_cena(radky[5])
    }


def jidlo_a_cena(radek: str) -> dict:
    """Pomocna funkce pro oddeleni nazvu jidla a ceny"""
    *jidlo, cena = radek.split(' ')
    return {' '.join(jidlo): int(cena[:-2])}


def uloz_menu_do_json(slovnik: dict, nazev_souboru: str) -> None:
    with open(nazev_souboru, mode="w", encoding='cp1252') as json_soubor:
        json.dump(slovnik, json_soubor)


def vypis_do_konzole(tyden_slovnik, restaurace, oblibene_jidlo=''):
    W = '\033[0m'  # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    O = '\033[33m'  # orange
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple
    print(f"\n{restaurace:=^70}\n")
    for den, jidla in tyden_slovnik.items():
        print(f"{den:-^70}")
        for radek in jidla.values():
            nazev_jidla, cena = list(*radek.items())
            if oblibene_jidlo in nazev_jidla:
                print(f"• {R}{nazev_jidla} - {cena} Kc{W}")
            else:
                print(f"• {nazev_jidla} - {cena} Kc")


if __name__ == '__main__':
    main()