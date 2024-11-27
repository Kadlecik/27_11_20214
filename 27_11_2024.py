#task1

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Builder(Human):
    def __init__(self, name, age, gender, specialization):
        Human.__init__(self, name, age, gender)
        self.specialization = specialization

    def __str__(self):
        return f"{Human.__str__(self)}, Specialization: {self.specialization}"

class Sailor(Human):
    def __init__(self, name, age, gender, rank):
        Human.__init__(self, name, age, gender)
        self.rank = rank

    def __str__(self):
        return f"{Human.__str__(self)}, Rank: {self.rank}"

class Pilot(Human):
    def __init__(self, name, age, gender, license_type):
        Human.__init__(self, name, age, gender)
        self.license_type = license_type

    def __str__(self):
        return f"{Human.__str__(self)}, License Type: {self.license_type}"

# Příklad použití:
builder = Builder("John", 35, "Male", "Carpenter")
builder2 = Builder("Ondrej", 45, "Male", "specialista")
sailor = Sailor("Anna", 28, "Female", "Captain")
pilot = Pilot("Mike", 42, "Male", "Commercial")

print(builder)
print(builder2)
print(sailor)
print(pilot)

print()
#task2
class Passport:
    def __init__(self, passport_number, name, nationality, date_of_birth, expiration_date):
        self.passport_number = passport_number
        self.name = name
        self.nationality = nationality
        self.date_of_birth = date_of_birth
        self.expiration_date = expiration_date

    def __str__(self):
        return (f"Passport Number: {self.passport_number}, Name: {self.name}, "
                f"Nationality: {self.nationality}, Date of Birth: {self.date_of_birth}, "
                f"Expiration Date: {self.expiration_date}")

class ForeignPassport(Passport):
    def __init__(self, passport_number, name, nationality, date_of_birth, expiration_date, foreign_passport_number, visas):
        super().__init__(passport_number, name, nationality, date_of_birth, expiration_date)
        self.foreign_passport_number = foreign_passport_number
        self.visas = visas

    def __str__(self):
        visa_info = ", ".join(self.visas)
        return (f"{super().__str__()}, Foreign Passport Number: {self.foreign_passport_number}, "
                f"Visas: {visa_info}")

# Příklad použití:
passport = Passport("P123456", "John Doe", "Czech", "1990-01-01", "2030-01-01")
foreign_passport = ForeignPassport("P123456", "John Doe", "Czech", "1990-01-01", "2030-01-01", "FP654321", ["USA", "Canada"])

print(passport)
print(foreign_passport)
