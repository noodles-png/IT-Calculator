from modules.helpers import outro_prompt


def valid_ip(ip_input: int) -> bool:
    """ Checks if an IP address is valid
    Args:
        ip_input (str): IP address
    Returns: bool: True if valid, False if otherwise
        """
    segments = ip_input.split(".")
    if len(segments) != 4:
        return False
    for segment in segments:
        if not segment.isdigit():
            return False
        if not (0 <= int(segment) <= 255):
            return False
    return True


def ip_to_int(ip_input: int) -> int:
    """ Converts an IP address to an integer
    Args: ip_input (str): IP address
    Returns: int: The IP as a 32-bit integer
    """
    if valid_ip(ip_input):
        ip_segments = ip_input.split(".")
        int_result = (int(
            ip_segments[0]) * 256**3
            + int(ip_segments[1]) * 256**2
            + int(ip_segments[2]) * 256**1
            + int(ip_segments[3]) * 256**0
                     )
        return int_result
    else:
        print("Invalid IP address")
        return False


def int_to_ip(ip: int) -> int:
    """ Converts an integer to an IP address
    Args: ip (int): Integer to convert to an IP address
    Returns: IP address"""
    byte_1 = (ip >> 24) & 0xFF
    byte_2 = (ip >> 16) & 0xFF
    byte_3 = (ip >> 8) & 0xFF
    byte_4 = ip & 0xFF
    ip_string = f"{byte_1}.{byte_2}.{byte_3}.{byte_4}"
    return ip_string


def cidr_to_mask(prefix: int) -> int:
    """ Converts an IP address/CIDR to a mask in Bits
    Args: prefix (int): IP address/CIDR
    Returns: mask in bits
    """
    mask = 0xFFFFFFFF << (32 - prefix) & 0xFFFFFFFF
    return mask


def calculate_subnet(int_result: int, mask: int, prefix: int):
    """ Calculates the subnet mask and all network addresses
    Args:
        int_result (int): integer to use for all operations
        mask (int): mask to use
        prefix (int): prefix used to calculate the host amount
    Prints all subnet information
    """
    network_address = int_result & mask
    broadcast = int_result | (mask ^ 0xFFFFFFFF)
    host_begin = network_address + 1
    host_end = broadcast - 1
    host_amount = 2**(32 - prefix) - 2
    print(f"Netzadresse: {int_to_ip(network_address)}")
    print(f"Broadcast: {int_to_ip(broadcast)}")
    print(f"Subnet mask: {int_to_ip(mask)}")
    print(f"Host begin: {int_to_ip(host_begin)}")
    print(f"Host end: {int_to_ip(host_end)}")
    print(f"Host amount: {host_amount}")
    return {
        "network_address": int_to_ip(network_address),
        "broadcast": int_to_ip(broadcast),
        "subnet_mask": int_to_ip(mask),
        "host_begin": int_to_ip(host_begin),
        "host_end": int_to_ip(host_end),
        "host_amount": host_amount,
    }


def subnet_menu():
    """ CLI interface for subnetting module """
    while True:
        print("=== Subnetting Menu ===\n")
        ip_input = input("Enter an IP address/CIDR: ")
        ip, prefix = ip_input.split("/")
        prefix = int(prefix)
        int_result = ip_to_int(ip)
        mask = cidr_to_mask(prefix)
        subnet_result = calculate_subnet(int_result, mask, prefix)
        for i in subnet_result:
            print(f"{i}: {subnet_result[i]}")
        outro = outro_prompt()
        if outro == "again":
            continue
        elif outro == "menu":
            return
    return
