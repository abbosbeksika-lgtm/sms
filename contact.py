import re

class contact:
    def __init__(self, name, phone, email):
        if not re.fullmatch(r"^[a-z0-9_-]{3,15}$", name):
            raise ValueError("Ism noto‘g‘ri!")
        if not re.fullmatch(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", phone):
            raise ValueError("Telefon noto‘g‘ri!")
        if not re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", email):
            raise ValueError("Email noto‘g‘ri!")
        self.name = name
        self.phone = phone
        self.email = email

baza = []

def view():
    for i in baza:
        print(i)

def add():
    try:
        n = input("Name: ")
        p = input("Phone: ")
        e = input("Email: ")
        baza.append(contact(n, p, e))
        print("Kontakt qo‘shildi.\n")
    except Exception as x:
        print("Xato:", x)


def edit():
    view()
    i = int(input("Qaysi kontaktni tahrirlamoqchisiz?: "))
    if not (0 <= i < len(baza)):
        print("Bunday kontakt yoq.")
        return

    n = input("Yangi ism: ")
    p = input("Yangi tel: ")
    e = input("Yangi email: ")

    if n: 
        if re.fullmatch(r"^[a-z0-9_-]{3,15}$", n): baza[i].name = n
    if p:
        if re.fullmatch(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", p): baza[i].phone = p
    if e:
        if re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", e): baza[i].email = e
    print("Yangilandi.\n")

def delete():
    view()
    i = int(input("O‘chirmoqchi bolganingizni tanlang: "))
    if 0 <= i < len(baza):
        baza.pop(i)
        print("Ochirildi.\n")
    else:
        print("Xato.")

def manager():
    while True:
        kod = input("1.Korish \n2.Qoshish \n3.Tahrirlash \n4.Ochirish \n5.Chiqish \n: ")
        if kod == '1': view()
        elif kod == '2': add()
        elif kod == '3': edit()
        elif kod == '4': delete()
        else: break

manager()
