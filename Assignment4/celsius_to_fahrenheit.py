# F = (F - 32) * 5/9
# C = (C * 9/5) + 32

ZERO_C = -273.15

# Input validation loop
while (user_input := int(input("Enter a Celsius degree: "))) < ZERO_C:
    print("Enter a input above absolute zero!")
else:
    print(f"{"Celsius":<20} {"Fahrenheit"}")

    # Horizontal Dashed line
    for n in range(42):
        print("-", end="")
    print()

    # Compute and display
    for n in range(0, user_input - 1, -1) if user_input < 0 else range(user_input + 1):
        print(f"{n:<20} {(n * 9/5) + 32:,.2f}")
