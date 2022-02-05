# Nyní bude tvým úkolem vytvořit funkci sum_list, která bude umět sečíst všechna čísla,
# která najde v listu - jak v číselné podobě, tak v textové. Skript by si měl poradit i v takovém případě,
# kdy v listu nebudou jen čísla. Pokud na takovou položku narazí, jednoduše ji přeskočí a bude pokračovat dál.
# Pro otestování skriptu můžeš vyzkoušet tento sequence:


test = [1, 'asda', {'zvire': 'kocka'}, '3.0', 2.0, [], '\n', '4']
# Výsledek je 10.


def sum_list(list_of_items) -> int:
    """
    function adds item to a 'summary' variable
    if it can be changed to float type. If error raises:
    :except will skip this value
    """
    summary = 0
    for item in list_of_items:
        try:
            summary += float(item)
        except (ValueError, TypeError):
            continue
    return summary


print(sum_list(test))
