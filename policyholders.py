class Policyholder:
    def __init__(self, name, surname, tel_number, age):
        self.name = name
        self.surname = surname
        self.tel_number = tel_number
        self.age = age

    def __str__(self):
        return f"{self.name}\t{self.surname}\t{self.age}\t{self.tel_number}"

class HolderList:
    def __init__(self):
        self.policyholders = []

    def display_policyholders(self):
        print("Seznam pojištěnců:\n")
        for policyholder in self.policyholders:
            print(policyholder)
        print("Pokračujte libovolnou klávesou...\n")
        input()
    def search_policyholder(self):
        search = input("Zadejte jméno nebo příjmení pojištěnce:")
        for policyholder in self.policyholders:
            if search.lower() in policyholder.name.lower() or search.lower() in policyholder.surname.lower():
                print(policyholder)
            else:
                print("Tohoto pojištěnce nemáme v evidenci.")
        print("Pokračujte libovolnou klávesou...\n")
        input()
