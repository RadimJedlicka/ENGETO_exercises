# K minulé úloze přidej následujíci:
#
# vytiskni jména na indexu od 2 do 5 za string: 'V intervalu od 2 do 5 je: ',
# vytiskni každý třetí prvek listu zamestnanci za string: 'Každý třetí člen je: ',
# vytiskni, na kterém indexu se nachází string 'Jakub' v listu zamestnanci za string: 'Jakub je na indexu: ',
# vytiskni, kolikrát se jméno 'Anežka' nachází v listu `zamestnanci za string: 'Počet jména Anežka v listu: '.

# Vylsedky z minule ulohy
kandidati = ['Anezka', 'Anezka', 'Anezka']
zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára', 'Anežka', 'Anežka', 'Anežka']

# Interval 2-5
print("V intervalu od 2 do 5 je:", zamestnanci[2:6])

# Kazdy 3.
print("Kazdy treti clen je:", zamestnanci[::3])

# Ulozeni indexu
print("Jakub je na indexu:", zamestnanci.index("Jakub"))

# Jakub index

# Anezka pocet
print("Pocet jmena Anezka v listu:", zamestnanci.count('Anežka'))
