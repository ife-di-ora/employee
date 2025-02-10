from pydantic import BaseModel, PositiveInt, Field
from typing import Literal


class Employee(BaseModel):
    id: PositiveInt 
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=18, lt=65)
    dept: str
    role: Literal['Manager', 'Developer', 'Designer', 'HR', 'Sales']
    salary: int = Field(..., gt=0)
