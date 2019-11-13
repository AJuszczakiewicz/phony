class DeleteServiceUpdate:
    def __init__(self, phonebook, contact_id):
        self.phonebook = phonebook
        self.contact_id = contact_id

    def run(self):
        contact = self.phonebook.get_contact_by_contact_id(self.contact_id)
        self.phonebook.contact_list.remove(contact)