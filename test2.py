class Person:
    def __init__(self, name, phone, age):
        self.name = name
        self.phone = phone
        self.age = age

    def show(self):
        print(f"name: {self.name}, phone: {self.phone}")

class Student(Person):
    def __init__(self, name, phone, age, student, group):
        super().__init__(name, phone, age)
        self.student = student
        self.group = group

    def show(self):
        print(f"name: {self.name}, Student_id: {self.student}, Group_id: {self.group}")

p1 = Person("Ali", "1234567", 12)
s1 = Student("Vali", "23451232", 24, 7564321234, 53)
p1.show()
s1.show()
