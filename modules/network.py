# Bandwith units
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
def time_calc(value, value_unit, bandwith_size, bandwith_unit):
    size_unit = size_units[value_unit]
    bandwith_unit = bandwith_units[bandwith_unit]
    result = (value * size_unit) / (bandwith_size * bandwith_unit)
    return result

# calculates bits = bps * second
def size_calc(time_input, bandwith_size, bandwith_unit):
    time = int(time_input)
    bandwith_unit = bandwith_units[bandwith_unit]
    result = time * (bandwith_size * bandwith_unit)
    return result

# calculates bits per second (bps)
def bandwith_calc(value, value_unit, time_input):
    size_unit = size_units[value_unit]
    result = (value *value_unit) / time_input
    return result





def network_menu():
    while True:
        print("=== Network Calculator ===")
        print("Choose a Calculator")
        print("[1] Time\n[2] Size\n[3] Bandwith")
        calc_choice = input("Choose an option: ")
        if calc_choice == "1":
            value = float(input("Enter size: "))
            value_unit = input("Choose a unit: ")
            bandwith_size = float(input("Choose a bandwith: "))
            bandwith_unit = input("Choose a unit: ")
            result = time_calc(value, value_unit, bandwith_size, bandwith_unit)
            print(result)
        elif calc_choice == "2":
            size_calc()
        elif calc_choice == "3":
            bandwith_calc()
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