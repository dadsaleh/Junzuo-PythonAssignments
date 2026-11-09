import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Illinois": "Springfield",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Michigan": "Lansing",
    "Nevada": "Carson City",
    "New York": "Albany",
    "Ohio": "Columbus",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Texas": "Austin",
    "Vermont": "Montpelier",
    "Washington": "Olympia",
}


def main():
    correct = 0
    incorrect = 0
    exit_flag = False

    while not exit_flag:
        # Select random state
        key = random.choice(list(capitals))

        # Prompt user
        while (
            resp := input(
                f"What is the capital of {key}? (or enter 0 to quit): "
            ).lower()
        ) != "0":
            if resp == capitals[key].lower():
                print("That is correct")
                correct += 1
                break
            else:
                print("That is incorrect")
                incorrect += 1
                break
        if resp == "0":
            exit_flag = True
    print(f"You had {correct} correct responses and {incorrect} incorrect responses")


if __name__ == "__main__":
    main()
