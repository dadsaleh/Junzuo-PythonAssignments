from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

TEMPERATURE_FILE = Path(__file__).resolve().parent / "temperature_forloop.txt"

def main():
    celsius = get_celsius()

    # Search for the temperature using both loops
    fahrenheit_forloop = find_match_forloop(celsius)
    fahrenheit_whileloop = find_match_whileloop(celsius)
    print(f"For-loop search result:   {fahrenheit_forloop}")
    print(f"While-loop search result: {fahrenheit_whileloop}")

    if fahrenheit_forloop is not None:
        print(f"Match found: {celsius} Celsius is {fahrenheit_forloop:.2f} Fahrenheit.")
    else:
        fahrenheit = (celsius * 1.8) + 32
        append_record(celsius, fahrenheit)
        print(f"No match found. New record added: {celsius} Celsius = {fahrenheit:.2f} Fahrenheit.")

def get_celsius():
    # Input validation loop
    while (celsius := int(input(f"Enter a celsius degree ({MIN_CELSIUS}-{MAX_CELSIUS}): "))) < MIN_CELSIUS or celsius > MAX_CELSIUS:
        print(f"Invalid input. Please enter a temperature between {MIN_CELSIUS} and {MAX_CELSIUS}.")
    return celsius

def find_match_forloop(celsius):
    fahrenheit = None

    with open(TEMPERATURE_FILE, "r") as infile:
        skip_header(infile)
        for line in infile:
            degree_text, fahrenheit_text = line.split("\t\t")
            if int(degree_text) == celsius:
                fahrenheit = float(fahrenheit_text)
                break
    return fahrenheit

def find_match_whileloop(celsius):
    fahrenheit = None

    with open(TEMPERATURE_FILE, "r") as infile:
        skip_header(infile)
        line = infile.readline()
        while line != "":
            degree_text, fahrenheit_text = line.split("\t\t")
            if int(degree_text) == celsius:
                fahrenheit = float(fahrenheit_text)
                break
            line = infile.readline()
    return fahrenheit

def skip_header(infile):
    # skip the header and dashed line
    infile.readline()
    infile.readline()

def append_record(celsius, fahrenheit):
    with open(TEMPERATURE_FILE, "a") as outfile:
        outfile.write(f"{celsius:>8}\t\t{fahrenheit:>8.2f}\n")

if __name__ == "__main__":
    main()
