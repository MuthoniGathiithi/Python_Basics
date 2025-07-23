def get_average(grades):
    return sum(grades) / len(grades)
def grade_feedback(average):
    if average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

grades_input = input("Enter 5 grades separated by spaces: ")
grades = list(map(int, grades_input.split()))
average = get_average(grades)
grade = grade_feedback(average)
print(f"Your average score is: {average}")
print(f"Your grade is: {grade}")
