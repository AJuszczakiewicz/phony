from contact import Contact

class CreateContactService:
    def __init__(self, name, surname, phone_number, phone_type, phonebook):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.phone_type = phone_type
        self.phonebook = phonebook

    def run(self):
        build_result, contact = self._build_contact()
        if build_result:
            self.phonebook.add_contact(contact)
        return build_result, contact

    def _build_contact(self):
        contact = Contact(self.name, self.surname)
        contact.add_new_number(self.phone_number, self.phone_type)
        return True, contact

