from modules.helpers import outro_prompt, unit_choice

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

def format_time(seconds):
    """ Formats the time in certain time units

    Args:
        seconds: the time in seconds

    Returns:
        returns the formatted time in certain time units
    """
    if seconds >= 3600:
        return f"{seconds /3600:.2f} hours"
    elif seconds >= 60:
        return f"{seconds /60:.2f} minutes"
    elif seconds >= 1:
        return f"{seconds /1:.2f} seconds"
    else:
        return f"{seconds * 1000:.2f} milliseconds"


def time_calc(value, value_unit, bandwidth_size, bandwidth_unit):
    """ Calculates the time it takes to download a certain sized file

    Args:
        value: size of the file
        value_unit: size unit of the file
        bandwidth_size: size of the network bandwidth
        bandwidth_unit: size unit of the network bandwidth

    Returns: time in seconds
    """
    size_unit = size_units[value_unit]
    bandwidth_unit = bandwidth_units[bandwidth_unit]
    result = (value * size_unit) / (bandwidth_size * bandwidth_unit)
    return result


def size_calc(time_input, bandwidth_size, bandwidth_unit):
    """ Calculates the size of a file to be sent in a network
    Args:
        time_input: time in seconds
        bandwidth_size: size of the network bandwidth
        bandwidth_unit: size unit of the network bandwidth
    Returns: size in bytes """
    time = int(time_input)
    bandwidth_unit = bandwidth_units[bandwidth_unit]
    result = time * (bandwidth_size * bandwidth_unit)
    return result


def bandwidth_calc(value, value_unit, time_input):
    """ Calculates the size of the network bandwidth
    Args:
        value: size of the file
        value_unit: size unit of the file
        time_input: time in seconds
    Returns: size of the network bandwidth in bits per second
    """
    size_unit = size_units[value_unit]
    result = (value * size_unit) / time_input
    return result


def network_menu():
    """ CLI interface for network conversion """
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

        outro = outro_prompt()
        if outro == "again":
            continue
        elif outro == "menu":
            return
