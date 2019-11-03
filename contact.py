from phoneNumber import PhoneNumber

class Contact:
    id_count = 1

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.numbers = []
        self.id = Contact.id_count
        Contact.id_count += 1

    def add_new_number(self, number, type):
        phone_number = PhoneNumber(number, type)
        self.numbers.append(phone_number)

    def __str__(self):
        str_rep = f'name: {self.name}\nsurname: {self.surname}'
        for number in self.numbers:
            str_rep += f'\n{number}'
        return str_rep

