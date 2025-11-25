import re

def name_regex(name):
    return re.match(r'^[a-z0-9_-]{3,15}$', name)
def phone_regex(phone):
    return re.match(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', phone)
def email_regex(email):
    return re.match(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+', email)

class Student:
    def __init__(self, name, phone, age, email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email

class Group:
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.students = []

    def add_student(self):
        while True:
            name = input("Name: ")
            if name_regex(name):
                break
            print("Ism notogri.")
        while True:
            phone = input("Phone: ")
            if phone_regex(phone):
                break
            print("Tel raqam notogri.")
        while True:
            age = input("Age: ")
            if age.isdigit():
                break
            print("Yosh notogri kiritdingiz.")
        while True:
            email = input("Email: ")
            if email_regex(email):
                break
            print("Email notogri")
        self.students.append(Student(name, phone, age, email))
        print("Student qoshildi")

    def view_students(self):
        if len(self.students) == 0:
            print("==============")
            print("Talaba yo‘q")
            print("==============")
            return
        index = 1
        for i in self.students:
            print(f"{index}. Ism: {i.name} \n   Phone: {i.phone}\n   Yosh: {i.age}\n   Email: {i.email}")
            index += 1

class OTM:
    def __init__(self, title):
        self.title = title
        self.groups = []

    def add_group(self):
        title = input("Group name: ")
        profession = input("Profession: ")
        self.groups.append(Group(title, profession))

    def view_groups(self):
        if len(self.groups) == 0:
            print("==============")
            print("Guruhlar yoq")
            print("==============")
            return
        index = 1
        for i in self.groups:
            print(f"{index}. Group: {i.title}, Profession: {i.profession}")
            index += 1

class ERP:
    def __init__(self):
        self.otms = []
    def add_otm(self):
        title = input("OTM name: ")
        self.otms.append(OTM(title))

    def view_otms(self):
        if len(self.otms) == 0:
            print("OTM mavjud emas.")
            return
        index = 1
        for i in self.otms:
            print("==============")
            print(f"{index}. OTM: {i.title}")
            index += 1
            print("==============")

def group_manager(group):
    while True:
        kod = input("1. Add student\n2. View student\n3. Edit student\n4. Back\n : ")
        if kod == "1":
            group.add_student()
        elif kod == "2":
            group.view_students()
        elif kod =="3":
            if len(group.students) == 0:
                print("Talaba mavjud emas.")
                continue
            try:
                index = int(input("Student ID: "))
                s = group.students[index-1]
                print(f"Name: {s.name}, Phone: {s.phone}, Age: {s.age}, Email: {s.email}")
            except:
                print("Bunday ID mavjud emas.")
                continue

            while True:
                field = input("Qaysi birini tahrirlamoqchisiz? (name / phone / age / email / back): ").lower()
                if field == "name":
                    name = input(f"Name (oldingi name: {s.name}): ")
                    if name_regex(name):
                        s.name = name
                        print("Name yangilandi.")
                elif field == "phone":
                    phone = input(f"Phone (oldingi phone: {s.phone}): ")
                    if phone_regex(phone):
                        s.phone = phone
                        print("Phone yangilandi.")
                elif field == "age":
                    age = input(f"Age (oldingi yosh: {s.age}): ")
                    try:
                        if int(age) > 0:
                            s.age = age
                            print("Age yangilandi.")
                    except:
                        pass
                elif field == "email":
                    email = input(f"Email (oldingi email: {s.email}): ")
                    if email_regex(email):
                        s.email = email
                        print("Email yangilandi.")
                elif field == "back":
                    break
                else:
                    print("Notogri buyruq.")
        elif kod == "4":
            break
        else:
            print("Notogri buyruq.")

def otm_manager(otm):
    while True:
        kod = input("1. Add group\n2. View group\n3. Group details\n4. Back\n : ")
        if kod == "1":
            otm.add_group()
        elif kod == "2":
            otm.view_groups()
        elif kod == "3":
            if len(otm.groups) == 0:
                continue
            try:
                otm.view_groups()
                index = int(input("Group ID: "))
                group_manager(otm.groups[index-1])
            except:
                print("Bunday ID mavjud emas.")
        elif kod == "4":
            break
        else:
            print("Notogri buyruq.")

def erp_manager(erp):
    while True:
        kod = input("1. Add OTM\n2. View OTM\n3. OTM details\n4. Exit\n: ")
        if kod == "1":
            erp.add_otm()
        elif kod == "2":
            erp.view_otms()
        elif kod == "3":
            erp.view_otms()
            if len(erp.otms) == 0:
                continue
            try:
                index = int(input("OTM ID: "))
                otm_manager(erp.otms[index-1])
            except:
                print("Bunday ID mavjud emas.")
        elif kod == "4":
            break
        else:
            print("Notogri buyruq.")

erp = ERP()
erp_manager(erp)