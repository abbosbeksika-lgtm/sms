# class Student:
#     def __init__(self,name,phone,age):
#         self.name = name
#         self.phone = phone
#         self.age = age
#
# student1 = Student("Ali", "123456", 12)
# student2 = Student("Vali", "1234568", 15)
# student3 = Student("Sari", "1234567", 14)

# baza = [student1, student2, student3]

# print(f"name = {student1.name}, phone = {student1.phone}, age = {student1.age}")
# def view_students(s:list):
#     for item in s:
#         print(f'name:{item.name}, phone:{item.phone}, age:{item.age}')
# view_students(baza)"

# def add_student(s: list):
#     name = input("name:")
#     age = input("name:")
#     phone = input("name:")
#     studentw = Student(name, phone, age)
#     s.append(studentw)
#
# # add_student(baza)
# # view_students(baza)
#
# def student_manager(s: list):
#     while True:
#         kod = input(" 1.view student \n 2. add student \n 3. break")
#         if kod == '1':
#             view_students(s)
#         elif kod == "2":
#             add_student(s)
#         else:
#             break
#
#
# student_manager(baza)

"""
produckt managerni title, price, saqlash muddati, chqarilgan sana, type, email, phone
"""

class Product:
    def __init__(self, title, price, saqlash, sana, type, email, phone):
        self.title = title
        self.price = price
        self.saqlash = saqlash
        self.sana = sana
        self.type = type
        self.email = email
        self.phone = phone
maxsulot = Product("Asus", 1300, "cheksiz", "2020", "noutbuk", "asfbfd@gmail.com", +998911450512)
# print(student.title, student.price, student.sana, student.saqlash, student.type, student.email, student.phone)

baza = [maxsulot]

def view_product(s:list):
    for item in s:
        print(f'Title:{item.title}, Price:{item.price}, Saqlash: {item.saqlash}, sana:{item.sana}, type:{item.type}, email:{item.email}, phone:{item.phone}')
# view_product(baza)

def add_product(s:list):
    title = input("Title: ")
    price = input("Price: ")
    saqlash = input("Saqlash: ")
    sana = input("Chiqarilgan sana: ")
    type = input("Type: ")
    email = input("Email: ")
    phone = input("Phone: ")
    productview = Product(title, price, saqlash, sana, type, email, phone)
    s.append(productview)

def manager_product(s: list):
    while True:
        kod = input("1. view product \n2. add product \n3. tugatish.")
        if kod == '1':
            view_product(s)
        elif kod == '2':
            add_product(s)
        else:
            print("Dastur tugatildi")
            break
manager_product(baza)
