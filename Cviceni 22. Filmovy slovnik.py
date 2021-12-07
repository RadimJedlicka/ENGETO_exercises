# Vstupní proměnné
oddelovac = "=" * 66
sluzby = ("dostupne filmy", "detaily filmu", "reziseri", "doporuc film")
hodnoceni_uzivatelu = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
    )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

# Společný slovník 'filmy'
filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4
}

# Přihlášení, uvítání, nabídka (případně ukončení)
uzivatel = input("Zadejte sve jmeno: ")
# print("V poradku :-)") if uzivatel in hodnoceni_uzivatelu else print("Neregistrovany uzivatel!",
#                                                         "-program terminated-", sep="\n")
if uzivatel in hodnoceni_uzivatelu:
    print("V poradku :-)")
else:
    print("Neregistrovany uzivatel!", "-program terminated-".center(28), sep="\n")
    quit()

print(oddelovac, "VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(66), sep="\n")
print(oddelovac, f"Sluzby: | {' | ' .join(sluzby)}".center(66), oddelovac, sep="\n")

# Umožnit výběr ze služeb, výpis všech filmů a ukončení
vyber = input("Vyberte sluzbu z nabidky vyse: ")
if vyber in sluzby and vyber == 'dostupne filmy':
    print("Dostupne filmy: ", ', ' .join(filmy.keys()), oddelovac, sep="\n")

elif vyber == 'detaily filmu' and vyber in sluzby:
    print("Dostupne filmy:", ' - '.join(filmy.keys()))
    vybrany_film = input('Vyber film: ')
    if vybrany_film in filmy.keys():
        print(oddelovac, f'FILM: {vybrany_film}', sep="\n")
        print(filmy[vybrany_film], oddelovac, sep="\n")
    else:
        print('Takovy film neni ve slovniku', oddelovac, sep="\n")

elif vyber in sluzby and vyber == 'reziseri':
    reziseri = {filmy["Shawshank Redemption"]["REZISER"],
                filmy["The Godfather"]["REZISER"],
                filmy["The Dark Knight"]["REZISER"],
                filmy["The Prestige"]["REZISER"]}
    print(f"{', ' .join(reziseri)}", oddelovac, sep="\n")

elif vyber in sluzby and vyber == sluzby[3]:
    # kopie puvodniho hodnoceni (budeme upravovat!)
    kopie_hodnoceni = hodnoceni_uzivatelu.copy()
    print("Kopie hodnoceni: ", kopie_hodnoceni)

    # kdo je prihlasen?
    aktivni_uzivatel = kopie_hodnoceni.pop(uzivatel)
    print("Filmy aktivniho uzivatele: ", uzivatel, aktivni_uzivatel)

    # zbytek uzivatelu
    # kopie_hodnoceni.pop(uzivatel)   ---- to tu asi byt nemusi?
    # zbytek_hodnoceni = kopie_hodnoceni  ----- to jenom, kdyz si chci zbyvajici seznam ulozit pod novou promennou,
                                                                    # ale diky .pop uz tam neni "aktivni uzivatel
    print("Zbytek hodnoceni po vyrazeni aktivniho uzivatele: ", kopie_hodnoceni)

    detaily_prvni_uzivatel = kopie_hodnoceni.popitem()
    print(detaily_prvni_uzivatel)
    detaily_druhy_uzivatel = kopie_hodnoceni.popitem()
    print(detaily_druhy_uzivatel)

    print(kopie_hodnoceni)

    # # jmena a filmy zbyvajicich uzivatelu
    jmeno_prvni_uz, filmy_prvni_uz = detaily_prvni_uzivatel
    jmeno_druhy_uz, filmy_druhy_uz = detaily_druhy_uzivatel
    print(jmeno_prvni_uz)

    # porovnani spolecnych filmu
    spolecny_s_prvnim = aktivni_uzivatel.intersection(filmy_prvni_uz)
    spolecny_s_druhym = aktivni_uzivatel.intersection(filmy_druhy_uz)
    print(f"Spolecne filmy s {jmeno_prvni_uz}: {spolecny_s_prvnim}")
    print(f"Spolecne filmy s {jmeno_druhy_uz}: {spolecny_s_druhym}")

    # vyber nejvetsiho poctu spolecnych filmu
    if len(spolecny_s_prvnim) > len(spolecny_s_druhym):
        nejvice_spolecnych = hodnoceni_uzivatelu[jmeno_prvni_uz]
        winner = jmeno_prvni_uz
    elif len(spolecny_s_prvnim) < len(spolecny_s_druhym):
        winner = jmeno_druhy_uz
        nejvice_spolecnych = hodnoceni_uzivatelu[jmeno_druhy_uz]
    elif len(spolecny_s_prvnim) == len(spolecny_s_druhym):
        nejvice_spolecnych = hodnoceni_uzivatelu[jmeno_prvni_uz].union(hodnoceni_uzivatelu[jmeno_druhy_uz])
        winner = jmeno_prvni_uz + " a " + jmeno_druhy_uz
    print(f"Nejvice spolecnych filmu mas s {winner} a ten uz videl: {nejvice_spolecnych}")

    # navrhovane filmy (co videli ostatni a ja jeste ne)
    navrhy = nejvice_spolecnych.difference(aktivni_uzivatel)
    print(f"Uzivatel {winner} ti navrhuje, aby ses podival na {navrhy} ;-)")

else:
    print("Vybrana sluzba neni v nabidce, ukoncuji..", oddelovac, sep="\n")

# Výpis všech režisérů

