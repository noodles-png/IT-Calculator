from modules.helpers import outro_prompt

# validates the user input
def valid_ip(ip_input):
    segments = ip_input.split(".")
    if len(segments) != 4:
        return False
    for segment in segments:
        if not segment.isdigit():
            return False
        if not (0 <= int(segment) <= 255):
            return False
    return True

# converts the ip address to an integer
def ip_to_int(ip_input):
    if valid_ip(ip_input) == True:
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

# converts a number to an ip address
def int_to_ip(ip):
    byte_1 = (ip >> 24) & 0xFF
    byte_2 = (ip >> 16) & 0xFF
    byte_3 = (ip >> 8) & 0xFF
    byte_4 = ip & 0xFF
    ip_string = f"{byte_1}.{byte_2}.{byte_3}.{byte_4}"
    return ip_string

# interprets the CIDR notation as subnetting mask
def cidr_to_mask(prefix):
    mask = 0xFFFFFFFF << (32 - prefix) & 0xFFFFFFFF
    return mask

def calculate_subnet(int_result, mask, prefix):
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

# takes the user input for conversion
def subnet_menu():
    while True:
        print("=== Subnetting Menu ===\n")
        ip_input = input("Enter an IP address/CIDR: ")
        ip, prefix = ip_input.split("/")
        prefix = int(prefix)
        int_result = ip_to_int(ip)
        mask = cidr_to_mask(prefix)
        calculate_subnet(int_result, mask, prefix)
        outro = outro_prompt()
        if outro == "again":
            continue
        elif outro == "menu":
            return
    return
