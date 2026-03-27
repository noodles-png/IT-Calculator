# Bandwidth units
bandwidth_units = {
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
def unit_choice(units):
    unit_index = list(units.keys())
    for i, unit in enumerate(unit_index, start=1):
        print(f"[{i}] {unit}")
    choice = int(input("Choose a unit: ")) -1
    return unit_index[choice]


# menu for network.py
def network_menu():
    while True:
        print("=== Network Calculator ===")
        print("Choose a Calculator")
        print("[1] Time\n[2] Size\n[3] Bandwidth")
        calc_choice = input("Choose an option: ")
        if calc_choice == "1":
            value = float(input("Enter size: "))
            value_unit = unit_choice(size_units)
            bandwidth_size = float(input("Choose a bandwidth: "))
            bandwidth_unit = unit_choice(bandwidth_units)
            result = time_calc(value, value_unit, bandwidth_size, bandwidth_unit)
            print((format_time(result)))
        elif calc_choice == "2":
            time_input = float(input("Enter time in sec: "))
            bandwidth_size = float(input("Enter bandwidth: "))
            bandwidth_unit = unit_choice(bandwidth_units)
            result = size_calc(time_input, bandwidth_size, bandwidth_unit)
            print(f"{result:.2f} Bit")
        elif calc_choice == "3":
            value = float(input("Enter value: "))
            value_unit = unit_choice(value_unit)
            time_input = float(input("Enter time: "))
            result = bandwidth_calc(value, value_unit, time_input)
            print(f"{result:.2f} Bits per second")
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
