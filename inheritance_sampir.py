class person:
    def __init__(self, pid, name, age):
        self.name = name
        self.age = age

class student(person) :
    def __init__(self,pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id

class staff(person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id



student1 = student(11324561121234, "Alice", 20, "S12345")
staff1 = staff(123412563123, "Bob", 35, "ST67890")

print(f"Student Name: {student1.name}, Age: {student1.age}, Student ID: {student1.student_id}")
print(f"Staff Name: {staff1.name}, Age: {staff1.age}, Staff ID: {staff1.staff_id}")

def get_person_info(person):
    return f"Name: {person.name}, Age: {person.age}"

get_person_info(student1)
get_person_info(staff1)