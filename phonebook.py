from contact import Contact

class Phonebook:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, record):
        self.contact_list.append(record)

    def get_contact_by_contact_id(self, contact_id):
        for contact in self.contact_list:
            if contact.id == contact_id:
                return contact

    def __repr__(self):
        return self.contact_list

    def __str__(self):
        repr_str = ""
        for contact in self.contact_list:
            repr_str = repr_str + str(contact) + "\n\n"
        return repr_str
