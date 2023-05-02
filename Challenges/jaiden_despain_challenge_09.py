# Asking the user if they would likw to add a user to the gradebook.
def Menu():

    while True:
        add_student = input("Would you like to add a new student to the gradebook?  ")

        if add_student.lower() == "yes":
            AddStudent()
            break
        elif add_student.lower() == "no":
            print("Alright then, goodbye!")
            exit()
        else:
            print("(Please respond with 'yes' or 'no')")
            
# Adding a student and their grades.
def AddStudent():
    student_name = input("What is the student's name?  ")
    entered_grades = input("What are the student's grades?  ")

    # Converting the entered grades into integers and putting them into a list.
    student_grades = [int(i) for i in entered_grades.split()]

    StudentGradebook(student_name, student_grades)

# List of students.
def StudentGradebook(name, grade_value):
    grade_book = {'Ica': [100, 90, 95] , 'Gina': [90, 88, 94], 'McClump': [74, 83, 11]}

    grade_book[name] = grade_value
    print(grade_book)

# Main function.
def main():
    Menu()

main()
