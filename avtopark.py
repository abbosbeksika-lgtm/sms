class Car:
    def __init__(self, name, year, price_per_day):
        self.name = name
        self.year = year
        self.price_per_day = price_per_day
        self.is_rented = False

class User:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.rented_cars = []

class Rentkompany:
    def __init__(self, title):
        self.title = title
        self.balance = 0
        self.cars = []
        self.rented_cars = []

    def add_car(self):
        name = input("Car name: ")
        year = int(input("Year: "))
        price = int(input("Price per day: "))
        car = Car(name, year, price)
        self.cars.append(car)
        print("Mashina qoshildi.\n")
    print("-------------------")

    def edit_car(self):
        self.view_all_cars()
        index = int(input("Qaysi mashinani tahrirlaysiz? index: ")) -1
        if index < 0 or index >= len(self.cars):
            print("Xato index.\n")
            return

        car = self.cars[index]
        print("Nimani ozgartirasiz?")
        print("1. Name\n2. Year\n3. Price per day")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            car.name = input("New name: ")
        elif tanlov == "2":
            car.year = int(input("New year: "))
        elif tanlov == "3":
            car.price_per_day = int(input("New price: "))
        else:
            print("Xato tanlov.")

    def view_all_cars(self):
        print("\n--- Barcha mashinalar ---")
        i = 1
        for car in self.cars:
            if car in self.rented_cars:
                holat = "Ijarada"
            else:
                holat = "Bosh"
            print(f"{i}. {car.name}, {car.year}, {car.price_per_day}, {holat}")
            i += 1
        print("-------------")

    def bosh_mashinalar(self):
        print("\n--- bosh mashinalar ---")
        for car in self.cars:
            if car not in self.rented_cars:
                print(f"{car.name}, {car.year}, {car.price_per_day}")
        print("-------------")

    def view_rented_cars(self):
        print("\n--- Ijaradagi mashinalar ---")
        for car in self.rented_cars:
            print(f"{car.name}, {car.year}, {car.price_per_day}")
        print()

    def rent_car(self, user: User):
        self.bosh_mashinalar()
        name = input("Qaysi mashinani olmoqchisiz? name: ")
        car = None
        for i in self.cars:
            if i.name == name:
                car = i
                break
        if not car:
            print("Bunday mashina yoq.\n")
            return
        if car in self.rented_cars:
            print("Bu mashina ijarada.\n")
            return
        days = int(input("Necha kun?: "))
        total_price = car.price_per_day * days
        print(f"{car.name} mashinasi uchun {days} kunlik ijara: {total_price}")
        if user.salary < total_price:
            print("Oylik yetmaydi. Mashina berilmaydi.\n")
            return
        self.rented_cars.append(car)
        user.rented_cars.append(car)
        self.balance += total_price
        print("Mashina ijaraga berildi.\n")

    def return_car(self, user: User):
        if not user.rented_cars:
            print("Userda mashina yoq.\n")
            return
        print("--- Mashina ijarada ---")
        i = 1
        for car in user.rented_cars:
            print(f"{i}. {car.name}")
            i += 1
        index = int(input("Qaysi mashinani qaytarasiz?: ")) - 1
        if index < 0 or index >= len(user.rented_cars):
            print("Xato index.\n")
            return
        car = user.rented_cars.pop(index)
        self.rented_cars.remove(car)
        print("Mashina qaytarildi.\n")


def manager(company: Rentkompany, user: User):
    while True:
        kod = input(" -------------------- \n1. Car qo'shish\n2. Car tahrirlash\n3. Barcha mashinalar\n4. Bosh mashinalar\n5. Ijaradagi mashinalar\n6. Ijaraga olish\n7. Mashinani qaytarish\n8. Exit\n: ")
        if kod == "1":
            company.add_car()
        elif kod == "2":
            company.edit_car()
        elif kod == "3":
            company.view_all_cars()
        elif kod == "4":
            company.bosh_mashinalar()
        elif kod == "5":
            company.view_rented_cars()
        elif kod == "6":
            company.rent_car(user)
        elif kod == "7":
            company.return_car(user)
        else:
            print("Dastur tugatildi.")
            break

company = Rentkompany("RENT")
company.cars.append(Car("Malibu", 2022, 300))
company.cars.append(Car("Gentra", 2021, 150))
company.cars.append(Car("Tracker", 2023, 400))
company.cars.append(Car("Damas", 2019, 80))
company.cars.append(Car("Cobalt", 2020, 180))

users = []
while True:
    print("1. Yangi user \n2. Oldingi user bilan davom etish \n3. Chiqish")
    choise = input("Tanlang: ")
    if choise == "1":
        name = input("Ism: ")
        surname = input("Familiya: ")
        salary = int(input("Maosh: "))
        current_user = User(name, surname, salary)
        users.append(current_user)
        manager(company, current_user)
    elif choise == "2":
        if not users:
            print("Hali user yoq\n")
            continue
        s = 1
        for user in users:
            print(f"{s}. {user.name} {user.surname}")
            s += 1
        index = int(input("user index kiriting: ")) - 1
        current_user = users[index]
        manager(company, current_user)
    else:
        print("Dastur tugatildi.")
        break

manager(company, current_user)
