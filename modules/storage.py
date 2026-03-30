from modules.helpers import outro_prompt, unit_choice

# decimal units (SI)
dec_units = {
    "bit": 0.125,
    "byte": 1,
    "kb": 1000,
    "mb": 1000000,
    "gb": 1000000000,
    "tb": 1000000000000,
    "pb": 1000000000000000
}

# binary units
bi_units = {
    "bit": 0.125,
    "byte": 1,
    "kib": 1024,
    "mib": 1048576,
    "gib": 1073741824,
    "tib": 1099511627776,
    "pib": 1125899906842624
}

def storage_conv(value, from_unit, to_unit, mode):
    """ Returns the conversion of either decimal or binary bases and size units
    Args:
        value (float): value to convert
        from_unit (str): size unit from which to convert
        to_unit (str): unit from which to convert
        """
    if mode == "1":
        units = dec_units
    elif mode == "2":
        units = bi_units
    else:
        print("Invalid mode")
        return None

    from_factor = units[from_unit]
    to_factor = units[to_unit]
    result = value * from_factor / to_factor
    return result

def storage_menu():
    """ CLI interface for storage module"""
    while True:
        print(f"=== Storage units conversion ===\n")
        print("Which output mode?")
        print(f"\n[1] Decimal units\n[2] Binary units\n")
        mode = input("Enter your choice: ")
        if mode == "1":
            units = dec_units
        elif mode == "2":
            units = bi_units
        else:
            print("Invalid mode")
            return None

        value = float(input("Enter your number: "))
        from_unit = unit_choice(units)
        to_unit = unit_choice(units)
        result = storage_conv(value, from_unit, to_unit, mode)
        print("=== Results ===")
        print(f"\n{value}{from_unit} = {result}{to_unit}")
        outro = outro_prompt()
        if outro == "again":
            continue
        elif outro == "menu":
            return
