"""
Employee Management System using Dataclasses

This Python program manages employee records using dataclasses. It provides functionalities to add, display, search,
update, and remove employees. Additionally, employees can be sorted by name and their data can be saved to and loaded
from a file.

Usage:
- Run the script.
- Choose from the menu options to perform various operations on employee records.

"""

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    department: str
    salary: float

employee_list = []

def add_employee():
    """Add a new employee to the system."""
    name = input('Enter employee name: ')
    age = int(input('Enter employee age: '))
    department = input('Enter employee department: ')
    salary = float(input('Enter employee salary: '))
    employee = Employee(name, age, department, salary)
    employee_list.append(employee)
    print(name + ' added to the system.')

def display_employees():
    """Display details of all employees in the system."""
    if not employee_list:
        print('No employees in the system.')
    else:
        print('\nEmployee Details:')
        for employee in employee_list:
            print('Name: ' + employee.name + ', Age: ' + str(employee.age) + ', Department: ' + employee.department + ', Salary: $' + format(employee.salary, '.2f'))

def search_employee():
    """Search for an employee by name."""
    name = input('Enter the name of the employee to search: ')
    found = False
    for employee in employee_list:
        if employee.name.lower() == name.lower():
            print('\nEmployee Details:')
            print('Name: ' + employee.name + ', Age: ' + str(employee.age) + ', Department: ' + employee.department + ', Salary: $' + format(employee.salary, '.2f'))
            found = True
            break
    if not found:
        print("Employee with name '" + name + "' not found in the system.")

def update_employee():
    """Update an employee's salary by searching for them by name."""
    name = input('Enter the name of the employee to update: ')
    found = False
    for employee in employee_list:
        if employee.name.lower() == name.lower():
            new_salary = float(input('Enter the new salary: '))
            employee.salary = new_salary
            print(name + "'s salary updated to $" + format(new_salary, '.2f') + '.')
            found = True
            break
    if not found:
        print("Employee with name '" + name + "' not found in the system.")

def remove_employee():
    """Remove an employee from the system by searching for them by name."""
    name = input('Enter the name of the employee to remove: ')
    for employee in employee_list:
        if employee.name.lower() == name.lower():
            employee_list.remove(employee)
            print(name + ' removed from the system.')
            break
    else:
        print("Employee with name '" + name + "' not found in the system.")

def sort_employees():
    """Sort employees by name."""
    employee_list.sort(key=lambda x: x.name.lower())

def save_to_file():
    """Save employee data to a file."""
    with open('employee_data.txt', 'w') as file:
        for employee in employee_list:
            file.write(employee.name + ',' + str(employee.age) + ',' + employee.department + ',' + format(employee.salary, '.2f') + '\n')

def load_from_file():
    """Load employee data from a file."""
    try:
        with open('employee_data.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name, age, department, salary = data
                age = int(age)
                salary = float(salary)
                employee = Employee(name, age, department, salary)
                employee_list.append(employee)
        print('Employee data loaded from file.')
    except FileNotFoundError:
        print('No employee data file found.')

while True:
    print('\nEmployee Management System Menu:')
    print('1. Add Employee')
    print('2. Display Employees')
    print('3. Search Employee')
    print('4. Update Employee Salary')
    print('5. Remove Employee')
    print('6. Sort Employees by Name')
    print('7. Save Employee Data to File')
    print('8. Load Employee Data from File')
    print('9. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        add_employee()
    elif choice == '2':
        display_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        update_employee()
    elif choice == '5':
        remove_employee()
    elif choice == '6':
        sort_employees()
        print('Employees sorted by name.')
    elif choice == '7':
        save_to_file()
        print('Employee data saved to file.')
    elif choice == '8':
        load_from_file()
    elif choice == '9':
        print('Exiting Employee Management System. Goodbye!')
        break
    else:
        print('Invalid choice. Please select a valid option.')
