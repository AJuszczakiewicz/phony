from phonebook import Phonebook
from contact import Contact

class PhonebookFactory:
    def __init__(self, json_data):
        self.json_data = json_data

    def build(self):
        phonebook = Phonebook()
        for record in self.json_data:
            contact = Contact(record['name'], record['surname'])
            phonebook.add_contact(contact)
            for number in record['numbers']:
                contact.add_new_number(number['phone_number'],
                                       number['phone_type'])
        return phonebook
