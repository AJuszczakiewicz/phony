from view.ascii_graphics import WARNING


class DeleteContactService:
    def __init__(self, phonebook, contact_id):
        self.phonebook = phonebook
        self.contact_id = contact_id

    def run(self):
        ok = self.contact_id in [contact.id for contact in self.phonebook.contact_list]
        if ok:
            contact = self.phonebook.get_contact_by_contact_id(self.contact_id)
            self.phonebook.contact_list.remove(contact)
        else:
            print(WARNING)
            print("Action aborted. Wrong contact ID number\n\n")
