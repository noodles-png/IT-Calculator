# Bandwidth units
bandwith_units = {
    "bps": 1,
    "kbps": 1000,
    "mbps": 1000000,
    "gbps": 1000000000,
    "tbps": 1000000000000
}

# Size units
size_units = {
    "bit": 1,
    "byte": 8,
    "kb": 8000,
    "mb": 8000000,
    "gb": 8000000000,
    "tb": 8000000000000,
}

# formats sec into min or ms
def format_time(seconds):
    if seconds >= 3600:
        return f"{seconds /3600:.2f} hours"
    elif seconds >= 60:
        return f"{seconds /60:.2f} minutes"
    elif seconds >= 1:
        return f"{seconds /1:.2f} seconds"
    else:
        return f"{seconds * 1000:.2f} milliseconds"

# calculates time = bits % bps
def time_calc(value, value_unit, bandwidth_size, bandwidth_unit):
    size_unit = size_units[value_unit]
    bandwidth_unit = bandwidth_units[bandwidth_unit]
    result = (value * size_unit) / (bandwidth_size * bandwidth_unit)
    return result

# calculates bits = bps * second
def size_calc(time_input, bandwidth_size, bandwidth_unit):
    time = int(time_input)
    bandwidth_unit = bandwidth_units[bandwidth_unit]
    result = time * (bandwidth_size * bandwidth_unit)
    return result

# calculates bits per second (bps)
def bandwidth_calc(value, value_unit, time_input):
    size_unit = size_units[value_unit]
    result = (value * size_unit) / time_input
    return result

# chooses unit choice via index choice
def unit_choice(unit_db):
    if unit_db == 1:
        unit_index = list(size_units.keys())
        for i, unit in enumerate(unit_index, start=1):
            print(f"[{i}] {unit}")
        choice = input("Choose a unit: ")
        unit_result = unit_choice(choice)
        return unit_result
    elif unit_db == 2:
        unit_index = list(bandwidth_units.keys())
        for i, unit in enumerate(unit_index, start=1):
            print(f"[{i}] {unit}")
        choice = input("Choose a unit: ")
        unit_result = unit_choice(choice)
        return unit_result
    else:
        print("Invalid input")

# menu for network.py
def network_menu():
    while True:
        print("=== Network Calculator ===")
        print("Choose a Calculator")
        print("[1] Time\n[2] Size\n[3] Bandwidth")
        calc_choice = input("Choose an option: ")
        unit_db = calc_choice
        if calc_choice == "1":
            value = float(input("Enter size: "))
            value_unit = input("Choose a unit: ")
            unit_choice(value_unit)
            value_unit = unit_choice(value_unit)
            bandwidth_size = float(input("Choose a bandwidth: "))
            unit_db = 2
            bandwidth_unit = input("Choose a unit: ")
            unit_choice(bandwidth_unit)
            bandwidth_unit = unit_choice(bandwidth_unit)
            result = time_calc(value, value_unit, bandwidth_size, bandwidth_unit)
            print((format_time(result)))
        elif calc_choice == "2":
            time_input = float(input("Enter time: "))
            bandwidth_size = float(input("Choose a bandwidth: "))
            bandwidth_unit = input("Choose a unit: ")
            result = size_calc(time_input, bandwidth_size, bandwidth_unit)
        elif calc_choice == "3":
            value = float(input("Enter value: "))
            value_unit = input("Choose a unit: ")
            time_input = float(input("Enter time: "))
            result = bandwidth_calc(value, value_unit, time_input)
        else:
            print("Invalid input")
            continue

        outro_choice = input("[1] Again or [2] main menu? ")
        if outro_choice == "1":
            continue
        elif outro_choice == "2":
            return
        else:
            print("Invalid input")

network_menu()