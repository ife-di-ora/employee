from .models import Employee
from faker import Faker

# Create an employee manager class that will manage the employees
class EmployeeManager:
    def __init__(self):
        self.employees = []

# Class Method to Add an employee to the list of employees   
    def add_employee(self, employee):
        for emp in self.employees:
            if emp['id'] == employee['id']:
                raise ValueError(f'An employee with id: {emp['id']} already exists')
        self.employees.append(employee)

# Class Method to get an employee from the list of employees     
    def get_employee(self, employee_id):
        for employee in self.employees:
            if employee['id'] == employee_id:
                print (employee)
        return None
    
# Class Method to get all employees from the list of employees
    def get_all_employees(self):
        print (self.employees)

def main():
    try:
# An instance of faker to test data
        faker = Faker()
        employee_manager = EmployeeManager()

        #Add five random employees
        for x in range(5):
            employee = Employee (
                id=faker.random_int(min=1, max=4),
                name=faker.name().strip(),  
                age=faker.random_int(min=18, max=65),
                dept=faker.job().strip(),
                role=faker.random_element(elements=['Manager', 'Developer', 'Designer', 'HR', 'Sales']),
                salary=faker.random_int(min=1000, max=10000)
            ).model_dump()
            employee_manager.add_employee(employee)
        
        # Get all employees
        employee_manager.get_all_employees()
        # Search for employee with id of 1
        employee_manager.get_employee(1)
        
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()