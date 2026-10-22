import os # for handle file reading flexibly
import matplotlib.pyplot as plt # for using matplotlib to create graphs

# Name of the text file created by precipitation_analysis.py.
INPUT_FILE = "precipitation.txt"

def main():
    months, precipitation = read_precipitation_file(INPUT_FILE)

    if len(months) > 0:
        show_bar_chart(months, precipitation)

def read_precipitation_file(filename):
    # Read lines in the form month,amount and return two lists: months and precipitation
    months = []
    precipitation = []

    # Look for the file in the same folder as this program.
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    try:
        with open(path, 'r') as input_file:
            for line in input_file:
                (month, value) = line.split(",")
                months.append(month)
                precipitation.append(float(value))
    except FileNotFoundError:
        print(f"Could not find '{filename}'. Run precipitation_analysis.py first.")
    except ValueError:
        print(f"'{filename}' is not in the expected 'month,amount' format.")
        months = []
        precipitation = []

    return months, precipitation

def show_bar_chart(months, precipitation):
    # Use the first three letters of each month name so the labels fit.
    short_names = [month[:3] for month in months]

    plt.bar(short_names, precipitation)
    plt.title("Monthly Precipitation")
    plt.xlabel("Month")
    plt.ylabel("Precipitation")
    plt.show()

# Call the main function only if this file is run directly.
if __name__ == '__main__':
    main()

