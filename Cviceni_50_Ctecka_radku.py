# Tvým úkolem bude vytvořit funkci. Funkce bude číst soubor a také bude umět ošetřit případ, kdy soubor není nalezen.

# Co musí funkce splňovat
    # Jako argument vezme cestu k souboru.
    # Přečte soubor.
    # Zavře soubor.
    # Pokud soubor existuje, vrátí list, ve kterém bude každá položka reprezentovat jeden řádek souboru.
    # Pokud soubor neexistuje, funkce vrátí prázdný list a vypíše zprávu: Soubor xxx nebyl nalezen!


cesta_souboru = 'C:\\Python310\\ENGETO\\Jupyter Notebook\\09_text_files\\novy.txt'


def reading_function(path):
    try:
        with open(path) as file:
            obsah = file.readlines()
            print(obsah)
    except FileNotFoundError:
        file_name = path.split('\\')[-1]
        print(f'File {file_name} was not found!')


reading_function(cesta_souboru)
