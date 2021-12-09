# names = ['Michal', 'Pepa', 'Honza',
#         'Pavel', 'Lukas', 'Matej',
#         'Iva', 'Klara', 'Jana',
#         'Honza', 'Vasek','Milan', 'Michal']
# names = ["Beta", "Zora", "Adela", "Pavel", "Bob", "Richard"]
# names = ["Adela", "Beta", "Bob", "Pavel", "Richard", "Zora"]
names = [1, 2, 11 , 3, 4, 15, 6, 77, 8]
# print(names)

# Vytvoř list, do kterého vložíš jeden prvek z list `names`. Zároveň ho z listu `names` odstraň. Tento krok se ti bude hodit, když budeš chtít přidávat _ seřazovat další jméno z listu `names` do listu `sorted_names`
sorted_names = [names.pop(0)]
print(names)
print(sorted_names)
print("-" * 50)

# Začni vnější for loop, kterým budeš procházet seznam `names` (měl by mít už o jeden prvek méně)
for from_original in names:
    # Zační vnitřní for loop, kterým budeš procházet seznam `sorted_names` _ pomocí podmínkového výrazu, `break` _ `else` vlož jméno z `names` buď na pozici, nebo za pozici daného jméno v listu `sorted_names`
    for index0,from_sorted in enumerate(sorted_names):
        if from_original < from_sorted:
            sorted_names.insert(index0,from_original)
            break

    else:
        sorted_names.append(from_original)

# Vytiskni seřazená jména
print(sorted_names)