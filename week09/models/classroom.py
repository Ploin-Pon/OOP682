class classroom:
    def __init__(self, name, age = None):
        self.name = name
        self.age = age
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    def __str__(self):
        return f'Classroom: {self.name}, Age: {self.age}, Students: {len(self.students)}'