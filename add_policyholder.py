from policyholders import Policyholder
# funkce vytváří nového pojištěnce

def create_policyholder(holder_list):

    name = input("Zadejte křestní jméno:\n").strip().upper()
    while not name.isalpha():
        name = input("Zadejte pouze písmena.\n").strip().upper()
    surname = input("Zadejte příjmení:\n").strip().upper()
    while not surname.isalpha():
        surname = input("Zadejte pouze písmena.").strip().upper()

    tel_number = input("Zadejte telefonní číslo (9 číslic):\n").strip()
    while not tel_number.isdigit() or len(tel_number) !=9:
        tel_number = input("Zadat můžete pouze 9 čísel.\n").strip()

    age = input("Zadejte věk (2 čísla):\n").strip()
    while not age.isdigit() or len(age) !=2:
        age = input("Zadat můžete pouze 2 čísla.\n").strip()
    age = int(age)
    while age < 18 :
        age = int(input("Pojištěnec musí mít minimálně 18 let.\n"))

    new_policyholder = Policyholder(name, surname, tel_number, age)
    holder_list.policyholders.append(new_policyholder)
    print("Nový pojištěnec byl přidán. Pokračujte libovolnou klávesou...")
    input()



