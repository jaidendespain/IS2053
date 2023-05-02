import json

def companyRegistry(employee_name):

    # Reading the json database.
    with open('EmployeeDatabase.json', 'r') as file:
        data = json.load(file)

    # Checking for the employee in json database. 
    for employee in data['employees']:
        if employee['name'].lower() == employee_name.lower():

            # Employee found.
            return employee
        
    # Employee not found.
    return None
