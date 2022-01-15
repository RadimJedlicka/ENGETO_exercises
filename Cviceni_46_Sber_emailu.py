# Tvým úkolem je vytvořit několik funkcí, které budou pracovat dohromady v jednom programu.
# Výstup by měl být slovník který:

# pod klíčem 'emails_with_nums' obsahuje jen ty emaily extrahované z my_str, které v sobě mají numerické znaky,
# pod klíčem 'domains' obsahuje všechny domény extrahované z emailů z my_str (část emailu za symbolem @).

# Co by měly jednotlivé funkce dělat?

# Extrahovat všechny emaily z my_str.
# Posbírat všechny emaily obsahující numerické znaky.
# Extrahovat všechny domény.
#
# Ukázka běhu programu:
#
# $ python collect_emails.py
# {'domains': ['email.cz', 'info.com,', 'gmail.com', 'money.fr', 'info.cz.'],
# 'emails_with_nums': ['tiger123@email.cz', 'b2b@money.fr']}

from pprint import pprint

my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet.
'''


# Funkce pro posbirani emailu ze stringu
def extract_emails(text):
    splited = text.split()
    emails = []
    for string in splited:
        if '@' in string:
            string = string.strip(".,:!?")
            emails.append(string)
    return emails


# Funkce pro extrahovani emailu obsahujici cisla
def numbers_in_emails(emails):
    num_mails = set()
    for email in emails:
        for character in email:
            if character.isdigit():
                num_mails.add(email)
    return list(num_mails)


# Funkce pro extrahovani domen vsech emailu
def domains(emails):
    list_of_domains = []
    for email in emails:
        email = email.split('@')
        list_of_domains.append(email[1])
    return list_of_domains


def main():
    result = {
        'emails_with_nums': None,
        'domains': None
    }

    emails = extract_emails(my_str)

    result['emails_with_nums'] = numbers_in_emails(emails)
    result['domains'] = domains(emails)

    pprint(result)
    return result


main()
