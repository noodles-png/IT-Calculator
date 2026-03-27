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
        ip_segments = int(ip_input.split("."))
        int_result = ip_segments[0]*256**3 + ip_segments[1]*256**2 + ip_segments[2]*256**1 + ip_segments[3]*256**0
        return int_result



# converts a number to an ip address
def int_to_ip():


    byte_1 = (ip_input >> 24) & 0xFF
    byte_2 = (ip_input >> 16) & 0xFF
    byte_3 = (ip_input >> 8) & 0xFF
    byte_4 = ip_input & 0xFF


# takes the user input for conversion
def subnetting_menu():
    ip_input = input("Enter an IP address: ")
