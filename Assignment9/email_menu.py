import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Always read/write email.dat next to this script, regardless of the
# folder the program is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, "email.dat")


def main():
    """Load the emails, run the menu loop, and save after each change."""
    while (choice := get_user_choice()) != QUIT:
        emails = load_emails()  # Update each iter
        if choice == LOOK_UP:
            look_up(emails)
        if choice == ADD:
            add(emails)
        if choice == CHANGE:
            change(emails)
        if choice == DELETE:
            delete(emails)


def load_emails():
    """Load and return the saved emails dictionary (or an empty one)."""
    emails = {}
    try:
        with open(FILENAME, "rb") as f:
            while True:
                try:
                    emails = pickle.load(f)
                except EOFError:
                    break
            return emails
    except FileNotFoundError:
        return emails


def get_user_choice():
    """Display the menu and return a validated choice."""
    while True:
        print(
            "\n",
            "Menu",
            "\n" + "=" * 40,
            "\n" + "1. Look up and email address",
            "\n" + "2. Add a new name and email address",
            "\n" + "3. Change an existing email address",
            "\n" + "4. Delete a name and email address",
            "\n" + "5. Quit the program",
            "\n",
        )
        try:
            if LOOK_UP <= (choice := int(input("Enter your choice: "))) <= QUIT:
                if choice == QUIT:
                    return
                return choice
        except ValueError:
            continue


def look_up(emails):
    """Print the email address for a name the user enters, if found."""
    name = input("Enter a name: ")
    if (email := emails.get(name, None)) is None:
        print("The specified name was not found")
        return
    print(f"Name: {name}" + "\n", f"Email {email}")


def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    name = input("Enter name: ")
    if name in emails:
        print("Error: This name/address pair already exist, to update select 3")
        return
    email = input("Enter email address: ")  # No validation on this
    # Save to file
    emails[name] = email
    save_emails(emails)
    print("Name and address have been updated")


def change(emails):
    """Update the address for an existing name."""
    name = input("Enter a name: ")
    if name not in emails:
        print("Error: Name not found")
        return
    email = input("Enter the new address: ")
    emails[name] = email
    save_emails(emails)


def delete(emails):
    """Remove a name/address pair."""
    name = input("Enter name: ")
    if emails.pop(name, None) is None:
        print(f"Error: could find {name}")
        return
    # Update file:
    save_emails(emails)
    print(f"Removed {name}")


def save_emails(emails):
    """Pickle the emails dictionary to FILENAME."""
    with open(FILENAME, "wb") as f:  # File is created elsewise
        pickle.dump(emails, f)


if __name__ == "__main__":
    main()
