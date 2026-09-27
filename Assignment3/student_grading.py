# Declared Weightings
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2
EXAM_RANGE_MAX = 100
ASSIGNMENT_RANGE_MAX = 30
QUIZ_RANGE_MAX = 20

# Collect grades as floats
midterm_grade = float(input("Enter midterm grade 0-100: "))
final_exam_grade = float(input("Enter final exam grade 0-100: "))
assignment_one_grade = float(input("Enter assignment one grade 0-30: "))
assignment_two_grade = float(input("Enter assignment two grade 0-30: "))
quiz_one_grade = float(input("Enter quiz one grade 0-20: "))
quiz_two_grade = float(input("Enter quiz two grade 0-20: "))

# Compare and Compute avarages
# If, for the given type of assignment, is not within range, the boolean variable is set to that truth value and set the value to zero
exam_avarage = (
    ((midterm_grade + final_exam_grade) / 2) * EXAM_WEIGHT
    if not (
        is_bad_input_exam := not (
            (EXAM_RANGE_MAX >= midterm_grade >= 0)
            and (EXAM_RANGE_MAX >= final_exam_grade >= 0)
        )
    )
    else 0
)
assignment_avarage = (
    ((assignment_one_grade + assignment_two_grade) / 2) * ASSIGNMENT_WEIGHT
    if not (
        is_bad_input_assignment := not (
            (ASSIGNMENT_RANGE_MAX >= assignment_one_grade >= 0)
            and (ASSIGNMENT_RANGE_MAX >= assignment_two_grade >= 0)
        )
    )
    else 0
)
quiz_avarage = (
    ((quiz_one_grade + quiz_two_grade) / 2) * QUIZ_WEIGHT
    if not (
        is_bad_input_quiz := not (
            (QUIZ_RANGE_MAX >= quiz_one_grade >= 0)
            and (QUIZ_RANGE_MAX >= quiz_two_grade >= 0)
        )
    )
    else 0
)

# Compute only if there was no bad input ranges
# Else, print each bad input for the type of grade
if not ((is_bad_input_exam or is_bad_input_assignment) or is_bad_input_quiz):
    print(
        f"The students final grade is: {((exam_avarage / EXAM_RANGE_MAX) + (assignment_avarage / ASSIGNMENT_RANGE_MAX) + (quiz_avarage / QUIZ_RANGE_MAX)):.2%}"
    )
else:
    if is_bad_input_exam:
        print(
            f"Invalid input, please enter exams within the 0 - {EXAM_RANGE_MAX} range"
        )
    if is_bad_input_assignment:
        print(
            f"Invalid input, please enter assignments within the 0 - {ASSIGNMENT_RANGE_MAX} range"
        )
    if is_bad_input_quiz:
        print(
            f"Invalid input, please enter quizzes within the 0 - {QUIZ_RANGE_MAX} range"
        )
    print("The Students final grade is 0.00%")
