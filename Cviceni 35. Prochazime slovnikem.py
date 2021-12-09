# Vytvořte program, který vytiskne každý pár klíč-hodnota ve formátu: "Klíč: <key> | Hodnota: <value>"

film = {'name':'Forrest Gump',
        'made':1994,
        'director':'Robert Zemeckis',
        'soundtrack':'Multiple',
        'starring':'Tom Hanks',
        'fun_fact':'''The house used in Forrest Gump is the same house used in The Patriot (2000). Some paneling was changed for interior shots  in the latter film.'''}

for _ in film:
    print(f"Klic: {_} | Hodnota: {film.get(_)}")


# vzorove reseni z webu:
# Během každého opakování uvnitř smyčky chceme ze slovníku film extrahovat klíč i hodnotu.
# K tomu nám může pomoci metoda dict.popitem()
# Opakovaným prováděním dojde k vymazání celého slovníku, tudíž můžeme v hlavičce smyčky použít podmínku while film.
# Až bude slovník prázdný, kód ve smyčce nebude dále prováděn

# film = {'name':'Forrest Gump',
#         'made':1994,
#         'director':'Robert Zemeckis',
#         'soundtrack':'Multiple',
#         'starring':'Tom Hanks',
#         'fun_fact':'''The house used in Forrest Gump is the same house used in The Patriot (2000). Some paneling was changed for interior shots in the latter film.'''}
#
# while film:
#     info = film.popitem()
#     print('Key: ' + str(info[0]) + ' | Value: ' + str(info[1]))