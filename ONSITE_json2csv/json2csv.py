import os
import json
import csv
from pprint import pprint


def hlavni():
    cesta = 'C:\\Git\\ENGETO_exercises\\ONSITE_json2csv'
    json_to_csv(cesta)


def json_to_csv(cesta: str):
    """
    1. Najdeme json soubory
    2. nacteme obsah jsou souboru
    3. vybereme obsah polozek
    4. ulozime do csv
    """
    jsony = najdi_soubor_json('C:\\Git\\ENGETO_exercises\\ONSITE_json2csv')
    # print(jsony)
    obsah_jsonu = [nacti_obsah_jsonu(cesta, soubor) for soubor in jsony]
    # print(len(obsah_jsonu[0]))
    zadouci_klice = ['email', 'first_name', 'last_name']
    # print(fitruj_slovnik(obsah_jsonu[0][0], zadouci_klice))
    filtrovany_json = []
    for cast in obsah_jsonu:
        for slovnik in cast:
            filtrovany_json.append(filtruj_slovnik(slovnik, zadouci_klice))
    # pprint(filtrovany_json[:10])
    # pprint(filtruj_jmena(filtrovany_json, 'D'))
    zapis_do_csv('vystup.csv', filtrovany_json)


def najdi_soubor_json(adresar):
    """
    V zadanem adresari najdi vsechny soubory s koncovkou .sjon
    :param adresar:
    :return:
    """
    # soubory = os.listdir(adresar)
    # moje_json = []
    # for soubor in soubory:
    #     if os.path.splitext(soubor)[1] == '.json':  # [jmeno, koncovka]
    #         moje_json.append(soubor)
    # print(moje_json)
    return [soubor for soubor in os.listdir(adresar)     # list comprehension
            if soubor.endswith('.json')]


def nacti_obsah_jsonu(cesta: str, soubor: str) -> list:
    """
    Spoj cestu a nazev souboru a nacti json soubor do listu
    :param cesta: cesta k souboru
    :param soubor: ted nevim
    :return: list
    """
    with open(os.path.join(cesta, soubor)) as json_s:
        return json.load(json_s)


def filtruj_slovnik(slovnik: dict, zadouci_klice: list) -> dict:
    """
    Vyber ze slovniku jen ty klice, ktere jsou  seznamu 'zadouci klice'
    :param slovnik:
    :param zadouci_klice:
    :return:
    """
    upraveny_slovnik = dict()

    for klic in slovnik.keys():
        if klic not in zadouci_klice:
            continue
        else:
            upraveny_slovnik[klic] = slovnik[klic]
    return upraveny_slovnik


def filtruj_jmena(slovniky: list, zacin_na: str) -> list:
    """ Vyfiltrovat jmena zacinajici na zadane pismeno"""
    return [slovnik for slovnik in slovniky if slovnik['first_name'].startswith(zacin_na)]


def zapis_do_csv(soubor: str, udaje: list):
    """
    Do zadaneho souboru zapis filtrovane udaje ze seznamu slovniku
    Z prvniho indexu vem jmena klicu a pouzij je jako zahlavi pro csv
    :param soubor:
    :param udaje:
    :return:
    """
    zahlavi = udaje[0].keys()
    with open(soubor, 'w', encoding='utf-8', newline='') as csv_vystup:
        zapisovac = csv.DictWriter(csv_vystup, fieldnames=zahlavi)
        zapisovac.writeheader()
        zapisovac.writerows(udaje)        # konci '\n'
        print("Soubor zapsan na disk.")


if __name__ == '__main__':
    hlavni()
