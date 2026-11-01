from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent / "grades(in).csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    try:
        # Open File
        with open(GRADES_FILE, "r") as file:
            csv = file.readlines()

        # Small check to try to ensure csv delimited file
        for line in csv:
            line = line.strip("\n")
            for char in line:
                if (
                    (not char == ",")
                    and (not char.isnumeric())
                    and (not char.isalpha())
                ):
                    raise ValueError("Bad CSV")

        # Remove newline chars
        for i in range(len(csv)):
            csv[i] = csv[i].strip("\n")

        # Process Rows (skip the header)
        final_grades = []
        for i in range(1, len(csv)):
            final_grades.append(process_row(csv[i]))

        analyze_grade(final_grades)

    except FileNotFoundError:
        print("Error: grades file not found.")
    except Exception as err:  # noqa
        print("Error:", err)


def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""

    scores = [float(x) for x in row.split(",")[2:]]

    tests = scores[0:4]
    exams = scores[4:6]
    discussions = scores[6:8]
    project = scores[8]

    return weight_final(
        average_subject(tests),
        average_subject(exams),
        average_subject(discussions),
        project,
    )


def average_subject(subject_list):
    return sum(subject_list) / len(subject_list)


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    return (
        test_avg * TEST_WEIGHT
        + exam_avg * EXAM_WEIGHT
        + discussion_avg * DISCUSSION_WEIGHT
        + project_score * PROJECT_WEIGHT
    )


def analyze_grade(weight_final_list):
    count_90 = 0
    count_80 = 0
    count_70 = 0
    count_60 = 0
    count_below = 0

    for grade in weight_final_list:
        if grade >= 90:
            count_90 += 1
        elif grade >= 80:
            count_80 += 1
        elif grade >= 70:
            count_70 += 1
        elif grade >= 60:
            count_60 += 1
        else:
            count_below += 1

    print("Number of students with final grade 90 or above:", count_90)
    print("Number of students with final grade 80-89:", count_80)
    print("Number of students with final grade 70-79:", count_70)
    print("Number of students with final grade 60-69:", count_60)
    print("Number of students with final grade below 60:", count_below)


if __name__ == "__main__":
    main()
