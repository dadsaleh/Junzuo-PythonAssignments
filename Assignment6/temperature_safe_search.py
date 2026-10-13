from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

TEMPERATURE_FILE = Path(__file__).resolve().parent / "temperature_forloop.txt"


def main():
    celsius = get_celsius()

    fahrenheit_forloop = find_match_forloop(celsius)
    if fahrenheit_forloop is False:
        return

    print(f"For-loop search result:   {fahrenheit_forloop}")

    if fahrenheit_forloop is not None:
        print(f"Match found: {celsius} Celsius is {fahrenheit_forloop:.2f} Fahrenheit.")
    else:
        fahrenheit = (celsius * 1.8) + 32
        if append_record(celsius, fahrenheit):
            print(f"No match found. New record added: {celsius} Celsius = {fahrenheit:.2f} Fahrenheit.")


def get_celsius():
    # Validate the input as a whole number within range
    good_value_received = False
    while not good_value_received:
        celsius_text = input(f"Enter a celsius degree ({MIN_CELSIUS}-{MAX_CELSIUS}): ")
        try:
            celsius = int(celsius_text)
            if celsius < MIN_CELSIUS or celsius > MAX_CELSIUS:
                print(f"Invalid input. Please enter a temperature between {MIN_CELSIUS} and {MAX_CELSIUS}.")
            else:
                good_value_received = True
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    return celsius


def find_match_forloop(celsius):
    fahrenheit = None

    # Search the file and print an error if it cannot be read
    try:
        with open(TEMPERATURE_FILE, "r") as infile:
            skip_header(infile)
            for line in infile:
                degree_text, fahrenheit_text = line.split("\t\t")
                if int(degree_text) == celsius:
                    fahrenheit = float(fahrenheit_text)
                    break
    except FileNotFoundError:
        print("Temperature file not found. Run temperature_writing.py first.")
        return False
    except ValueError:
        print("The temperature file contains an invalid record.")
        return False
    except OSError as error:
        print(f"Could not read the data file: {error}")
        return False

    return fahrenheit


def skip_header(infile):
    infile.readline()
    infile.readline()


def append_record(celsius, fahrenheit):
    # add the new record to the file
    try:
        with open(TEMPERATURE_FILE, "a") as outfile:
            outfile.write(f"{celsius:>8}\t\t{fahrenheit:>8.2f}\n")
        return True
    except OSError as error:
        print(f"Could not write to the data file: {error}")
        return False


if __name__ == "__main__":
    main()
