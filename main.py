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
            cat_index += 1
            print(f"[{cat_index}] {category}")
        print("[Q] Beenden")

        # User Inputs choice of cateory
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(categories):
                choice_index = choice - 1
                chosen_category = categories[choice_index]
                print(chosen_category)
            else:
                print(f"{red}Input not valid{reset}")
                continue

        else:
            continue

if __name__ == "__main__":
    show_menu()

