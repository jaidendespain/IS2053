# Instructions

Create a dictionary with grades for several students. For example: grade_book = {'Gina': [100, 90, 95] , 'Tina': [90, 88, 94]}. Then, ask the user if they want to add a new student to the gradebook. If they say yes, allow the user to input the name of the student, followed by three grades. Finally, append the new user key:value to the grade_book dictionary.


Function Names:
Menu()
AddStudent()
StudentGradeBook(name, grade_value)


1. You will call Menu() from main, which is the if __name__ == '__main__':  part
2. Menu():  will simply ask the user if they want to add a new student to the gradebook.  If yes, then call AddStudent().  If no, then say goodbye and exit the program.     
3. AddStudent():    Ask the user for the student's name (the KEY) and their respective grades (values as a list).  I.e.  'Carlos': [90, 97, 85].  Pass the key:values to StudentGradeBook(name, grade_value). 
4. StudentGradeBook(name, grade_value):    Contains the grade_book dictionary.   After receiving the key:value pair, add it to the existing list and then print the new list to the console. 
