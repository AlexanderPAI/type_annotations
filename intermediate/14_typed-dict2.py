"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string

Note: school can be optional
"""
from typing import Optional, TypedDict


class Student(TypedDict, total=False):
    name: str
    age: int
    school: Optional[str]
