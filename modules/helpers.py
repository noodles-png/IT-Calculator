# central outro function for all modules
def outro_prompt():
    """ Loops the current function or goes back to the main menu """
    while True:
        outro_input = input("[1] Again or back to [2] Menu? ").strip()
        if outro_input == "1":
            return "again"
        elif outro_input == "2":
            return "menu"
        else:
            print("Invalid input. Please try again.")


def unit_choice(units):
    """ Returns a choice from the list of available units
    Args: units (list): list of available units
    Returns: unit_index (list): list of available units """
    unit_index = list(units.keys())
    for i, unit in enumerate(unit_index, start=1):
        print(f"[{i}] {unit}")
    choice = int(input("Choose a unit: ")) - 1
    return unit_index[choice]