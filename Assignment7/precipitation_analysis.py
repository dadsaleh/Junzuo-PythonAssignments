import os #os module to handle PATH flexibility for writing to the file

MIN_PRECIPITATION = 0.0

# Greatest monthly rainfall ever recorded: 366 inches, measured at
# Cherrapunji, Meghalaya, India, in July 1861 (Guinness World Records).
# Used as a generous upper bound since a reasonable "normal" range
# depends heavily on location.
MAX_PRECIPITATION = 366.0

# Name of the text file that stores the month names and precipitation amounts.
OUTPUT_FILE = 'precipitation.txt'


def main():
    # Create a list of the month names, January through December.
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    # Use the repetition operator to initialize the precipitation list with 0.0 for each month.
    precipitation = [0.0] * 12

    # Loop through the months and prompt the user for each month's precipitation.
    for i in range(len(months)):
        precipitation[i] = get_precipitation(months[i])

    # analyze the data using list methods and functions
    analyze_precipitation(precipitation, months)

    # Save each month name with its precipitation amount to a text file.
    path = write_precipitation_file(months, precipitation)
    print(f'Data saved to {path}')

"""
       Prompt the user to enter precipitation for the given month. Validate the input until a valid value is received.
       use try/except to capture ValueError, which can be resulted from text to float conversion.
"""
def get_precipitation(month):
    while True:
        try:
            while (MIN_PRECIPITATION > (i := float(input(f"Enter rainfall for the month {month}: ")))) or i > MAX_PRECIPITATION:
                print(f"Error: Invalid input, Enter precipitation between {MIN_PRECIPITATION} and {MAX_PRECIPITATION}")
            break # Break and return valid input
        except ValueError:
            print("Error: Please input a valid number")
        except Exception as err: # Unknown Error, can inf loop here, would exit
            print(f"Error: Unexpected Error {err}")
    return i

"""
       use list functions and methods to calculate annual precipitation total, average monthly precipitation, the highest 
       preciptiation and month, and the lowest precipitation and month
"""
def analyze_precipitation(precipitation, months):
    print(f"Total Rainfall: {(p := sum(precipitation)):.2f}")
    print(f"Average Rainfall: {p/12:.2f}")

    try:
        # Find the index for the max precipitation
        m = max(precipitation)
        i = precipitation.index(m)
        print(f"Highest rainfall: {months[i]}, {m:.2f}")

        # Do the same for min
        m = min(precipitation)
        i = precipitation.index(m)
        print(f"Lowest rainfall: {months[i]}, {m:.2f}")

    except ValueError:
        print("entered_unreachable_code: could not find valid index")
        return None

"""
       write the month and its preciptiation to the given file, in a format of for example
       January,3.25
       use try/except to capture OSError that can be raised in file writing (return None)
"""
def write_precipitation_file(months, precipitation, filename=OUTPUT_FILE):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    try:
        with open(path, 'w') as output_file:
            for i in range(len(months)):
                output_file.write(f"{months[i]},{precipitation[i]}\n")

    except OSError as error:
            print(f"Could not save the data to '{path}': {error}")
            return None
    return path


# Call the main function only if this file is run directly.
if __name__ == '__main__':
    main()

