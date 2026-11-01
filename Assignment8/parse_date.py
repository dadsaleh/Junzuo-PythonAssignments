months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while (date := _date(input("Enter a date in the format mm/dd/yyyy: "))) is None:
        continue
    print(date)


def _date(date: str) -> str | None:
    # Decline Empty String
    if date == " ":
        print("Error: Date must be in mm/dd/yyyy format with slashes")
        return

    # Get Tokens
    d = date.split("/")

    # Must be exactly 3 tokens, cannot be less than or greater than
    if len(d) != 3:
        print("Error: Date must be in mm/dd/yyyy format with slashes")
        return

    # Must be all numeric values, cannot be anything otherwise
    (month, day, year) = d[0], d[1], d[2]
    for value in (month, day, year):
        if not (value.isnumeric()):
            print("Error: Date must be in mm/dd/yyyy format with slashes")
            return

    # Day must be from 1 to 31, and month must be from 1 to 12
    if not (1 <= int(day) <= 31):
        print("Error: Day must be between 1 and 31")
        return
    if not (1 <= (month := int(month)) <= 12):
        print("Error: Month must be between 1 and 12.")
        return

    # Adjust for zero based list and return formatted string
    return months[month - 1] + f" {day}, " + year


if __name__ == "__main__":
    main()
