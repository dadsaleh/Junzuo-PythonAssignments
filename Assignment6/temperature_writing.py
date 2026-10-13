from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

# Set the output files in the same folder as the program
SCRIPT_DIR = Path(__file__).resolve().parent
FORLOOP_FILE = SCRIPT_DIR / "temperature_forloop.txt"
WHILELOOP_FILE = SCRIPT_DIR / "temperature_whileloop.txt"

def main():
    celsius = get_celsius()
    write_temperature_file_forloop(celsius)
    write_temperature_file_whileloop(celsius)

def get_celsius():
    # Input validation loop
    while (celsius := int(input(f"Enter a celsius degree ({MIN_CELSIUS}-{MAX_CELSIUS}): "))) < MIN_CELSIUS or celsius > MAX_CELSIUS:
        print(f"Invalid input. Please enter a temperature between {MIN_CELSIUS} and {MAX_CELSIUS}.")
    return celsius

def write_temperature_file_forloop(celsius):
    # Compute and write the temperatures to the file
    with open(FORLOOP_FILE, "w") as outfile:
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')
        outfile.write("------------------------------------\n")
        for degree in range(celsius + 1):
            fahrenheit = (degree * 1.8) + 32
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")

def write_temperature_file_whileloop(celsius):
    with open(WHILELOOP_FILE, "w") as outfile:
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')
        outfile.write("------------------------------------\n")
        degree = 0
        while degree <= celsius:
            fahrenheit = (degree * 1.8) + 32
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")
            degree += 1

if __name__ == "__main__":
    main()
