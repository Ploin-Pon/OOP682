'''from models.classroom import classroom
from models.student import Student

oop = classroom("OOP682")
oop.add_student(Student("Alice", 90))
oop.add_student(Student("Bob", 85))
print(f' all students in {oop.name}: {len(oop.students)}')
oop.add_student(Student("Charlie", 95))
print(f' all students in {oop.name}: {len(oop.students)}')'''

from models.classroom import classroom
from models.student import Student

oop = classroom("OOP682")

# ส่งให้ครบ: (ID, ชื่อ, อายุ, เกรด/คะแนน)
oop.add_student(Student("6801", "Alice", 20, 90))
oop.add_student(Student("6802", "Bob", 21, 85))

print(f' all students in {oop.name}: {len(oop.students)}')

oop.add_student(Student("6803", "Charlie", 19, 95))

print(f' all students in {oop.name}: {len(oop.students)}')