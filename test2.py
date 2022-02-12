# import csv
#
# prvni = ['Surname', 'Name', 'Full Name', 'Age', 'City', 'Job', 'Gender']
# obsah = [['Smith', 'John', 'Smith, John', '32', 'London', 'Programmer', ''],
# ['Doe', 'Joe', 'Doe, Joe', '34', 'Liverpool', '', 'Male'],
# ['Murphy', 'Ann', 'Murphy, Ann', '29', 'London', 'Admin', 'Female'],
# ['Cook', 'Floyd', 'Cook, Floyd', '28', '', 'Tester', 'Male'],
# ['Glenn', 'Taylor', 'Glenn, Taylor', '35', 'Birmingham', 'Manager', 'Female'],
# ['Mills', 'Amanda', 'Mills, Amanda', '41', 'Leicester', 'Quality Assurance', 'Female']]
#
# f = open('names.csv','w')
# f_writer = csv.writer(f)
#
# f_writer.writerow(prvni)
# f_writer.writerows(obsah)
#
# f.close()

# import csv
#
# f = open('test2.csv')
# # Vytváříme DictReader objekt.
# dict_reader = csv.DictReader(f, delimiter = ';')
# for i in dict_reader:
#     print(i)
# f.close()

# import csv
#
# dict1 = {'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London',
# 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}
# header = ['Surname', 'Name', 'Full Name', 'Age', 'City', 'Job', 'Gender']
#
# f = open('file.csv', 'w', newline='')
# writer = csv.DictWriter(f, header)
#
# writer.writeheader()
# writer.writerow(dict1)
#
# f.close()

# import json
# # Slovník který chceme zapsat
# employee = {'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London',
# 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}
# # Vyrábíme JSON string
# to_json = json.dumps(employee)
# # Otevíráme soubor a zapisujeme
# f = open('to_json', 'w')
# f.write(to_json)
# f.close()

# def is_isogram(string):
#     letters = []
#     for letter in string:
#         letters.append(letter.lower())
#     if len(list(letters)) == len(set(letters)):
#         return True
#     else:
#         return False
#
#
# # your code here
#
# print(is_isogram('oBba'))

def descending_order(num):
    # Bust a move right here
    cislo = str(num)
    seznam = []
    for c in cislo:
        seznam.append(c)

    seznam.sort(reverse=True)
    return ''.join(seznam)


print(descending_order('51'))