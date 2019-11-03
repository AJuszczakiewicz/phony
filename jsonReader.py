import json
from contact import Contact
from phonebook import Phonebook

class JsonReader:
    def __init__(self, file_name="phonebook.json"):
        self.file_name = file_name
        self.json_data = {}

    def read_file(self):
        with open(self.file_name, "r") as read_file:
            data = json.load(read_file)
        self.json_data = data

    def load_data(self):
        self.read_file()
        phonebook = Phonebook()
        for record in self.json_data:
            contact = Contact(record['name'], record['surname'])
            phonebook.add_contact(contact)
            for number in record['numbers']:
                contact.add_new_number(number['phone_number'],
                                       number['phone_type'])
        return phonebook