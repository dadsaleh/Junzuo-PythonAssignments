# F = (F - 32) * 5/9
# C = (C * 9/5) + 32

ABS_ZERO_F = -459.67
ABS_ZERO_C = -273.15


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)


def get_temperature_type():
    while (temperature_type := input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ")) != "C" and temperature_type != "F":
        print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
    return temperature_type


def get_temperature(temperature_type):
    if temperature_type == "F":
        minimum = ABS_ZERO_F
    else:
        minimum = ABS_ZERO_C

    while (temperature := float(input("Enter the temperature you want to convert: "))) <= minimum:
        print(f"Invalid temperature. Please enter a temperature above absolute zero ({minimum}).")
    return temperature


def display_conversion(temperature_type, temperature):
    if temperature_type == "F":
        result = (temperature - 32) * 5 / 9
        print(f"The temperature in Celsius is: {result:.2f}")
    else:
        result = temperature * 9 / 5 + 32
        print(f"The temperature in Fahrenheit is: {result:.2f}")


if __name__ == "__main__":
    main()
