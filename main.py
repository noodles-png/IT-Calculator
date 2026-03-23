from modules.numbers import number_menu
from modules.storage import storage_menu
#from modules.network import network_menu

# Farbdefinitionen
green = "\033[92m"
red = "\033[91m"
bold = "\033[1m"
reset = "\033[0m"

# Main menu options
categories = [
    "Numbers",
    "Storage",
    "Network",
    "Subnetting",
]

# Main menu function
def show_menu():
    while True:
        print(f"{green}{bold}=== IT-Rechner ==={reset}")
        for cat_index, category in enumerate(categories, start=1):
            print(f"[{cat_index}] {category}")
        print("[Q] Beenden")

        # User Inputs choice of category
        choice = input("Choose an option: ").strip().lower()
        if choice == "q":
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(categories):
                if choice == 1:
                    number_menu()
                elif choice == 2:
                    storage_menu()
                elif choice == 3:
                    network_menu()
            else:
                print(f"{red}Input not valid{reset}")
                continue

        else:
            continue

if __name__ == "__main__":
    show_menu()

