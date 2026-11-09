words = {}


def main():
    filename = input("Enter the name of the input file: ")
    with open(filename, "r") as f:
        for line in f:
            line = line.split()
            for word in line:
                # Note: No cleanup here
                if words.get(word, None) is None:
                    words[word] = 0
                words[word] += 1
    print(
        f"{'Words':20}",
        "Occurences",
        "\n" + "=" * 40,
    )
    for word, occurance in words.items():
        print(f"{word:20} {occurance}")


if __name__ == "__main__":
    main()
