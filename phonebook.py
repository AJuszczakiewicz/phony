class Phonebook:
    def __init__(self):
        self.contact_list = []

    def add_record(self, record):
        self.contact_list.append(record)

    def __repr__(self):
        return self.contact_list
