import csv
import datetime
import os

import requests
from bs4 import BeautifulSoup

# response = requests.get('https://httpbin.org')

# print(response.status_code)

# print(response.text)

# print(response.json)

# response = requests.post('http://httpbin.org/post', data = {'my_message':'Hello'})
#
# print(response.status_code)
#
# print(response.text)
#
# print(response.json)



# getr = requests.get('http://example.com/')
# # print(getr.text)
#
# soup = BeautifulSoup(getr.text, 'html.parser')
# # print(soup)
# #
# # print(soup.p)
# # print(soup.a)
#
# print(soup.body.div.contents)
# print(type(soup.body.div.contents))
#
# for child in soup.body.children:
#     print(child)
#
# for i, descendant in enumerate(soup.div.descendants):
#     print(f'DESCENDANT {i}: {descendant}')
#
# print(soup.find_all('p'), '\n')
# print(soup.find_all(charset="utf-8"))

# response = requests.get('https://markets.businessinsider.com/commodities/gold-price')
# # print(response.text)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
# cena_zlata = soup.find('span', {'class': 'price-section__current-value'})
# print(cena_zlata.text)
#
# datum_a_cas = datetime.datetime.now()
# print(datum_a_cas)
#
# with open('zlato.scv', mode='w', encoding='utf-8') as output:
#     zapis = csv.DictWriter(output, fieldnames=cena_zlata)
#     zapis.writeheader()
#     zapis.writerows(cena_zlata)
#     print('file written')

def request_gold_price():
    r = requests.get('https://markets.businessinsider.com/commodities/gold-price')
    soup = BeautifulSoup(r.text, "html.parser")
    price = soup.find('span', {'class': 'price-section__current-value'}).string
    print(f'The current price is {price}')

    # chars = []
    # for char in price:
    #     if char != ',':
    #         chars.append(char)
    #
    # price = ''.join(chars)
    return price

# request_gold_price()


# date_time()


def write_data(price):
    mode = 'w' if 'gold_price.csv' not in os.listdir() else 'a'

    with open('gold_price.csv', mode, encoding='utf-8', newline='') as  file:
        writer = csv.writer(file)
        # writer.writeheader('price', 'time')
        writer.writerow([price, datetime.datetime.now().strftime('%d.%m.%Y %H:%M')])

write_data(request_gold_price())