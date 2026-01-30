from models.person import Person
from models.student import Student
from models.staff import Staff

class Person:
  def __init__(self, pid, name, age):
    self.pid = pid
    self.name = name
    self.age = age

def __str__(self):
  return f'Person {self.pid}, {self.name}, {self.age}'