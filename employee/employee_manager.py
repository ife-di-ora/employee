from .models import Employee
from faker import Faker
import uuid

# Create an employee manager class that will manage the employees
class EmployeeManager():
    def __init__(self):
        self.employees = []

# Class Method to Add an employee to the list of employees   
    def add_employee(self, employee):
        for emp in self.employees:
            if emp.employee_id == employee.employee_id:
                raise ValueError('Employee already exists')
        self.employees.append(employee)

# Class Method to get an employee from the list of employees     
    def get_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None
    
# Class Method to get all employees from the list of employees
    def get_all_employees(self):
        return self.employees

def main():
    try:
# An instance of faker to test data
        faker = Faker()
        employee = Employee (
            id=faker.random_int(min=1, max=1000),
            name=input('Enter Employee Name: ').strip(),
            age=faker.random_int(min=18, max=65),
            dept=faker.job().strip(),
            role=faker.random_element(elements=['Manager', 'Developer', 'Designer', 'HR', 'Sales']),
            salary=faker.random_int(min=1000, max=10000)
        )
        employee_manager = EmployeeManager()
        employee_manager.add_employee(employee)
        print(employee_manager.employees)
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()