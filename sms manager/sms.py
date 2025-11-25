import re

class Contact:
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

class ContactManager:
    def __init__(self):
        self.contacts = []

    def view(self):
        if not self.contacts:
            print("Kontaktlar bazasi bosh.\n")
            return
        for idx, c in enumerate(self.contacts, 1):
            print(f"{idx}. Name: {c.name}, Phone: {c.phone}, Email: {c.email}")
        print()

    def add(self):
        try:
            n = input("Name: ")
            p = input("Phone: ")
            e = input("Email: ")
            self.contacts.append(Contact(n, p, e))
            print("Kontakt qoshildi.\n")
        except Exception as x:
            print("Xato:", x, "\n")

    def edit(self):
        self.view()
        i = int(input("Qaysi kontaktni tahrirlamoqchisiz?: ")) - 1
        if not (0 <= i < len(self.contacts)):
            print("Bunday kontakt yoq.\n")
            return
        n = input("Yangi ism: ")
        p = input("Yangi tel: ")
        e = input("Yangi email: ")
        if n:
            if re.fullmatch(r"^[a-z0-9_-]{3,15}$", n):
                self.contacts[i].name = n
        if p:
            if re.fullmatch(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", p):
                self.contacts[i].phone = p
        if e:
            if re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", e):
                self.contacts[i].email = e
        print("Yangilandi.\n")

    def delete(self):
        self.view()
        i = int(input("Ochirmoqchi bolganingizni tanlang: ")) - 1
        if 0 <= i < len(self.contacts):
            self.contacts.pop(i)
            print("Ochirildi.\n")
        else:
            print("Xato.\n")

    def is_exist(self, phone):
        for c in self.contacts:
            if c.phone == phone:
                return True
        return False

    def manager(self):
        while True:
            kod = input("1.Korish \n2.Qoshish \n3.Tahrirlash \n4.Ochirish \n5.Chiqish \n: ")
            if kod == '1': self.view()
            elif kod == '2': self.add()
            elif kod == '3': self.edit()
            elif kod == '4': self.delete()
            else: break


class SMS:
    def __init__(self, to_phone, message):
        self.to_phone = to_phone
        self.message = message

class SMSManager:
    def __init__(self, contact_manager):
        self.sms_baza = []
        self.contact_manager = contact_manager

    def send_sms(self):
        s = input("Kimga yuborilsin (Phone kiriting): ")
        if not self.contact_manager.is_exist(s):
            print("Kontakt mavjud emas, SMS yuborilmadi.\n")
            return
        x = input("SMS matni: ")
        self.sms_baza.append(SMS(s, x))
        print("SMS yuborildi.\n")

    def view_sms(self):
        if not self.sms_baza:
            print("SMSlar mavjud emas.\n")
            return
        for idx, s in enumerate(self.sms_baza, 1):
            print(f"{idx}. To: {s.to_phone}, Message: {s.message}")
        print()

    def delete_sms(self):
        self.view_sms()
        i = int(input("Qaysi SMSni ochirmoqchisiz?: ")) - 1
        if 0 <= i < len(self.sms_baza):
            self.sms_baza.pop(i)
            print("SMS o'chirildi.\n")
        else:
            print("Xato.\n")

    def manager(self):
        while True:
            kod = input("1.Yuborish\n2.Yuborilgan SMSlar\n3.Ochirish\n4.Chiqish\n: ")
            if kod == '1': self.send_sms()
            elif kod == '2': self.view_sms()
            elif kod == '3': self.delete_sms()
            else: break

def main_manager():
    cm = ContactManager()
    sm = SMSManager(cm)
    while True:
        kod = input("1.SMS Manager\n2.Contact Manager\n3.Chiqish\n: ")
        if kod == '1':
            sm.manager()
        elif kod == '2':
            cm.manager()
        else:
            print("Dastur tugatildi.")
            break

main_manager()
