
class Phonebook:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, record):
        self.contact_list.append(record)

    def get_contact_by_contact_id(self, contact_id):
        for contact in self.contact_list:
            if contact.id == contact_id:
                return contact

    def delete_contact_by_contact_id(self, contact_id):
        contact = self.get_contact_by_contact_id(contact_id)
        del contact

    def add_number_to_existing_contact(self, contact_id, phone_number, phone_type):
        contact = self.get_contact_by_contact_id(contact_id)
        contact.add_new_number(phone_number, phone_type)

    def __repr__(self):
        return self.contact_list

    def __str__(self):
        repr_str = ""
        for contact in self.contact_list:
            repr_str = repr_str + str(contact) + "\n"
        return repr_str