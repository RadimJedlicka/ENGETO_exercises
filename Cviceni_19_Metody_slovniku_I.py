# vytvor prazdne slovniky do slovníků
muj_slovnik = {}
novy_slovnik = {}

muj_slovnik.update(jmeno = "Karin")
muj_slovnik.update(prijmeni = "Gojer")

muj_tuple = "vek", "e-mail"
novy_slovnik = novy_slovnik.fromkeys(muj_tuple)

muj_slovnik2 = muj_slovnik.copy()
muj_slovnik2.update(novy_slovnik)

muj_slovnik2["vek"] = 55
muj_slovnik2["e-mail"] = "radim@jedi.com"

print("Muj puvodni slovnik", muj_slovnik)
print("Muj slovnik", muj_slovnik2)
print("Muj novy slovnik", novy_slovnik)