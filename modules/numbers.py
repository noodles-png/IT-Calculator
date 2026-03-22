# Converts non decimal into decimal
def to_decimal(chosen_digit, base):
    result = 0
    chosen_digit_length = len(chosen_digit) - 1
    base = int(base)

    for digit in chosen_digit:
        digital_value = digits.index(digit)
        dec_digit_var = digital_value*base**chosen_digit_length
        result += dec_digit_var
        chosen_digit_length -= 1
    return result

# Converts decimal into binary or hexadecimal
def from_decimal(chosen_digit, base):
    value = chosen_digit
    hex_value = (chosen_digit)
    result = ""
    if value == 0:
        return "0"
    while value > 0:
        rest = value % base
        result = digits[rest] + result
        value = value // base
    return result


# Input from user
print(f"=== Number conversion ===\n")
print("\nDecimal or not decimal?")
print("\n[1] Decimal\n[2] Non-decimal")
user_choice = input("Enter your choice: ")

digits = "0123456789abcdef"

if user_choice == "1":
    base = int(input("Enter the target base: "))
    user_input = int(input("Enter the number: "))

    # Non-decimal Output
    result = from_decimal(user_input, base)
    print(result)

if user_choice == "2":
    base = input("Enter the base (2 or 16): ")
    user_input = input("Enter the number: ")

    # Decimal Output
    result = to_decimal(user_input.strip().lower(), base)
    print(result)






