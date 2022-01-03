# Vytvoř skript, který:
#
# vyžádá jméno od uživatele _ uloží jej do proměnné jmeno,
# vytiskne proměnnou jmeno,
# vyžádá přijmení od uživatele _ uloží jej do proměnné prijmeni,
# vytiskne proměnnou prijmeni,
# vytvoří proměnnou cele_jmeno, do které uložíš spojení proměnné jmeno _ prijmeni oddělené mezerou,
# vytiskne proměnnou delka_jmena, která bude obsahovat hodnotu délky celého jména
# vytiskne proměnnou cele_jmeno, která bude shora i zespoda ohraničená řadami rovnítek.
# K tomu použij operaci opakování, znak = použij v každé řadě tolikrát, kolik znaků obsahuje string uložen v proměnné cele_jmeno

# Ukladani jmena
jmeno = input("Zadejte jmeno: ")

# Tisk jmena
print(jmeno)

# Ukladani prijmeni
prijmeni = input("Zadejte prijmeni: ")

# Tisk prijmeni
print(prijmeni)

# Vytvoreni _ tisk promenne cele_jmeno
cele_jmeno = jmeno + " " + prijmeni
print(cele_jmeno)
# Vytvoreni _ tisk promenne delka_jmena
delka_jmena = len(jmeno + prijmeni)
print(delka_jmena)
# Tisk ohranicene promenne cele_jmeno
print("=" * int(delka_jmena))
print(cele_jmeno)
print("=" * int(delka_jmena))