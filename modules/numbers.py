# Converts non decimal into decimal
def to_decimal(chosen_digit, base):
    digits = "0123456789abcdef"
    result = 0
    chosen_digit_length = len(chosen_digit) - 1

    for digit in chosen_digit:
        digital_value = digits.index(digit)
        dec_digit_var = digital_value*base**chosen_digit_length
        result += dec_digit_var
        chosen_digit_length -= 1
    return result

# Converts decimal into binary or hexadecimal
def from_decimal(chosen_digit, base):
    digits = "0123456789abcdef"
    value = chosen_digit
    result = ""
    if value == 0:
        return "0"
    while value > 0:
        rest = value % base
        result = digits[rest] + result
        value = value // base
    return result

def is_valid(user_input):
    digits = "0123456789"
    allowed = set(digits[ :base])
    return all(c in allowed for c in user_input )

def number_conversion():
    while True:
        # Input from user
        print(f"=== Number conversion ===\n")
        print("\nDecimal or not decimal?")
        print("\n[1] Decimal\n[2] Non-decimal")
        user_choice = input("Enter your choice: ")

        # Non-decimal Output
        if user_choice == "1":
            user_input = input("Enter the number: ").strip()
            if user_input.isdigit():
                user_input = int(user_input)
                print(f"\nYour number: {user_input}")
                print("------------------")
                print(f"Binär: {from_decimal(user_input, 2)}")
                print(f"Octal: {from_decimal(user_input, 8)}")
                print(f"Hexadecimal: {from_decimal(user_input, 16)}")
                outro_choice = input("[1] Again or [2] main menu? ")
                if outro_choice == "1":
                    continue
                elif outro_choice == "2":
                    return
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
                continue

        # Decimal Output
        elif user_choice == "2":
            base = int(input("Enter the base (2 or 16): "))
            user_input = input("Enter the number: ")
            if is_valid(user_input):
                print(f"Dezimal: {to_decimal(user_input, base)}")
                outro_choice = input("[1] Again or [2] main menu? ")
                if outro_choice == "1":
                    continue
                elif outro_choice == "2":
                    return
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
                continue

        else:
            print("Invalid input")
            continue
    return



