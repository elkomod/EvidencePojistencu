from add_policyholder import create_policyholder
from policyholders import HolderList
class Menu:
    def display_menu(self):
        print("-------------------------------------\n"
              "Evidence pojištěnců\n"
              "-------------------------------------")
        holder_list = HolderList()

        run_app = True

        while run_app:
            display_menu = True
            while display_menu:

                print("Vyberte si z následujích možností:")

                print("1 - Přidat nového pojištěnce")
                print("2 - Vypsat všechny pojištěnce")
                print("3 - Vyhledat pojištěnce")
                print("4 - Konec")
                choice = str(input("Napíšte číslo požadované akce: "))
                if choice == "1":
                    create_policyholder(holder_list)

                elif choice == "2":
                    holder_list.display_policyholders()

                elif choice == "3":
                    holder_list.search_policyholder()

                elif choice == "4":
                    print("Aplikace byla ukončena.")
                    run_app = False
                    display_menu = False
                else:
                    print("Zadaná volba "+choice,"je neplatná.")



menu = Menu()
menu.display_menu()


