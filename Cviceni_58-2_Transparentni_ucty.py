import csv
import sys

import requests
from bs4 import BeautifulSoup


# def parsing(url: str):
#     """
#     pomoci GET ziskame text z url adresy.
#     pomoci BeautifulSoup je vyparsujeme
#     :return:
#     """
#     response = requests.get(url)
#     parsed_soup = BeautifulSoup(response.text, 'html.parser', exclude_encodings='cp1252')
#     return parsed_soup
#
#
# print(parsing('https://ib.fio.cz/ib/transparent?a=2800396030'))
from requests import HTTPError


def make_soup(URL):

    r = requests.get(URL)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


print(make_soup('https://ib.fio.cz/ib/transparent?a=2800396030'))

