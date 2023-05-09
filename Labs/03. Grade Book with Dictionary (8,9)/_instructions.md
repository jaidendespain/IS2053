# Instructions

In this lab, you will create an Employee Database using a dictionary in Python. The database will include the names, salaries, job titles, home addresses, and contact information of employees. The catch is that the Employee Database will be stored in a separate file and imported into the file you will use to edit the database.


1. Create a file named EmployeeDatabase.py that contains the Employee Database, which should be a dictionary with the necessary employee information.
2. In a separate file named EmployeeDirectory.py, allow the user to read any item contained in the Employee Database. You can use any method you prefer, but you do not need to save anything to a file.


#### Functions and Files:
EmployeeDatabase,py

    A file that holds the employee database.

    Open the file, search it for the person's name, and return the key-value pairs to the calling function. The external file will only contain employee names and their respective attributes. You still need the EmployeeDatabase.py file to search for the value and return it to the EmployeeDirectory.py file.

    companyRegistry()

        This function will check if an employee's name is in the database and return their attributes to the calling function in EmployeeDirectory.py.

EmployeeDirectory.py

    Have a function that welcomes the user and determines what part of the database they would like to view. All you need to do is print the value associated with the field requested by the user. For instance, if I want to print out Andy's salary, it should only print the number associated with his salary. 
    
    The function can be called Menu(). This function will call the companyRegistry() function that is contained in the EmployeeDatabase.py file. Also, I would suggest using a try: catch block and putting that in a while loop. This way you can make sure the user inputs a persons name and not some other data type without crashing your program.  