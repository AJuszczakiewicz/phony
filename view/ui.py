from __future__ import print_function, unicode_literals

from PyInquirer import prompt
from examples import custom_style_3

from controller.create_contact_service import CreateContactService
from controller.delete_contact_service import DeleteContactService
from lib.phonebook_serializer import PhonebookSerializer
from view.ascii_graphics import MENU_TITLE
from view.ui_questions import add_contact_menu, delete_contact_menu, main_menu


class UI:

    def __init__(self, phonebook):
        self.phonebook = phonebook
        self.answers = {"main_menu": ""}

    def build(self):
        print(MENU_TITLE)
        self.main_menu()

    def run(self):
        self.build()

    def main_menu(self):
        while self.answers["main_menu"] != "Exit":
            self.answers = prompt(main_menu, style=custom_style_3)
            if self.answers["main_menu"] == "Show contacts":
                self.print_contacts()
            elif self.answers["main_menu"] == "Delete a contact":
                self.delete_contact_menu()
            elif self.answers["main_menu"] == "Add a new contact":
                self.add_new_contact()
            elif self.answers["main_menu"] == "Save to file":
                PhonebookSerializer(self.phonebook).run()

    def print_contacts(self):
        repr_str = """
                ========CONTACTS==========\n"""
        for contact in self.phonebook.contact_list:
            repr_str = repr_str + str(contact) + "\n\n"

        repr_str += """
                ==========================
                """
        print(repr_str)

    def delete_contact_menu(self):
        answers = prompt(delete_contact_menu, style=custom_style_3)
        if answers["delete"]:
            DeleteContactService(self.phonebook, answers["delete_contact_id"]).run()

    def add_new_contact(self):
        answers = prompt(add_contact_menu, style=custom_style_3)
        CreateContactService(answers["contact_name"],
                             answers["contact_surname"],
                             answers["contact_phone_number"],
                             answers["contact_phone_number_type"],
                             self.phonebook).run()
