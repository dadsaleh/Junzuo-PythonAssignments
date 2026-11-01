# Must be 8 chars long
# Must contain at least one upper
# May contain only letters and digits
MIN_LEN = 8


def main():
    while not (_is_valid(_ := input("Enter a password: "))):
        print("Password is invalid.")
    print("Password is valid")


def _is_valid(password: str) -> bool:
    if len(password) < MIN_LEN:
        print("Password Must be at least 8 characters long.")
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            continue
        if char.islower():
            has_lower = True
            continue
        if char.isupper():
            has_upper = True
            continue
        if (not (char.isalpha())) or char.isspace():
            print("Password cannot contain spaces or symbols")
            return False
    if not (has_upper and has_lower and has_digit):
        print(
            "Password must contain at least one uppercase letter, one lowercase letter, and one digit."
        )
        return False
    return True


if __name__ == "__main__":
    main()
