from EmployeeDatabase import companyRegistry

def Menu():
    # Asking for an employee's name.
    employee_name = input("Enter an employee name: ")

    # Making sure the employee is in the database.
    while True:
        employee = companyRegistry(employee_name)

        if employee is None:
            employee_name = input("Employee not found. Enter another: ")
        else:
            break


    # Asking the user for the information they want to view.
    information = input("Enter the information you would like to view (salary, title, address, or contact): ")

    # Making sure the information is in the database.
    while True:
        try:
            data = employee[information.lower()]
            break
        except KeyError:
            information = input("Please enter one of the above data types: ")


    # Printing the user's requested information.
    print(f"{employee['name']}'s {information.lower()} is {data}.")

Menu()
