from pydantic import BaseModel, PositiveInt, Field
from faker import Faker
from typing import Literal
# import uuid

faker = Faker()

class Employee(BaseModel):
    id: PositiveInt 
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=18, lt=65)
    dept: str
    role: Literal['Manager', 'Developer', 'Designer', 'HR', 'Sales']
    salary: int = Field(..., gt=0)

def main():
    employee = Employee (
        id=faker.random_int(min=1, max=1000),
        name=faker.name().strip(),
        age=faker.random_int(min=18, max=65),
        dept=faker.job().strip(),
        role=faker.random_element(elements=['Manager', 'Developer', 'Designer', 'HR', 'Sales']),
        salary=faker.random_int(min=1000, max=10000)
    )
    print(employee)

if __name__ == "__main__" :
    main()
