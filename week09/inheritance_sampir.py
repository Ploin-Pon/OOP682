from models.person import Person
from models.student import Student
from models.staff import Staff

def main():
  student = Student(123, 'pitcha', '0123')
  staff = Staff(124, 'pitchaeiei', '0123')
  print(f'Name {student.name}, Age {student.age}')
  print(f'Name {staff.name}, Age {staff.age}')

if __name__ == "__main__":
    main()