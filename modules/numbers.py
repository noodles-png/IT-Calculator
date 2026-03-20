import string

# Konvertiert Zahl in Dezimal
def to_decimal(chosen_digit, base):
    dec_number = 0
    chosen_digit_length = len(chosen_digit) - 1
    digits = (string.digits + string.ascii_lowercase)
    base = int(base)


    for digit in chosen_digit:
        digital_value = digits.index(digit)
        dec_digit_var = digital_value*base**chosen_digit_length
        dec_number += dec_digit_var
        chosen_digit_length -= 1
    return dec_number

#def from_decimal():

# Input from user
base = input("Enter the base (2 ro 16): ")
user_input = input("Enter the number: ")

# Output
result = to_decimal(user_input, base)
print(result)




