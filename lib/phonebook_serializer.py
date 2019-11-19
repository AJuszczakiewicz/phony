import json


class PhonebookSerializer:
    def __init__(self, phonebook):
        self.phonebook = phonebook
        self.data = []

    def prepare_data(self):
        person = {"numbers": []}
        for contact in self.phonebook.contact_list:
            person['name'] = contact.name
            person['surname'] = contact.surname
            number = {}
            for num in contact.numbers:
                number["phone_number"] = num.phone_number
                number["phone_type"] = num.phone_type
                person["numbers"].append(number)
            self.data.append(person)

    def run(self):
        self.prepare_data()
        with open("data/phonebook.json", "w") as write_file:
            json.dump(self.data, write_file)
