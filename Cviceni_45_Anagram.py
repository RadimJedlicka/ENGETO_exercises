# Když se dvě a více slov skládájí ze stejných znaků, které mají ale různé pořadí, říkame jim anagramy.
# Anagram určitého slova nebo fráze může vytvořit jiné slovo nebo frázi.
# Takže například anglické slovo 'eat' má v angličtině následující anagramy:
#
# ate
# tea
#
# Cílem tohoto cvičení je vytvořit funkci, která příjímá list dvou nebo více stringů jako vstup a vrací boolean hodnotu,
# která nám říká, jestli všechny prvky uvnitř listu jsou anagramy, nebo ne.
#
# Pokud vložíme prázdný string, výstup by měl být False.
# Pokud vložíme list s jedním slovem, výstup by měl být True.
#
# Příklad fungující funkce:
#
# >>> all_anagrams(['ship', 'hips'])
# True
# >>> all_anagrams(['ship', 'hips', 'name'])
# False
# >>> all_anagrams(['ship'])
# True
# >>> all_anagrams([])
# False

# MOJE RESENI NEFUNGUJE
# def all_anagrams(words):
#     if words == []:
#         return False
#     for slovo in words:
#         if sorted(slovo) == sorted(words[1:]):
#             return True
#         else:
#             return False

def all_anagrams(words):
    if words:
        result = True
        seq = sorted(words.pop())
        for word in words:
            if sorted(word) != seq:
                result = False
            else:
                result = True
    else:
        result = False
    return result


# Slova
words = ['ship','hips', 'spih', 'hisp', 'pihs']

# Volani fce
print( all_anagrams(words) )

# print(sorted(words[0]))
# print(sorted(words[1]))

# print(sorted(words[0]) == sorted(words[1]))