from __future__ import print_function, unicode_literals

from PyInquirer import Validator, ValidationError
from PyInquirer import prompt
from examples import custom_style_3

from controller.create_contact_service import CreateContactService
from controller.delete_contact_service import DeleteContactService
from view.ascii_graphics import MENU_TITLE


class UI:

    def __init__(self, phonebook):
        self.phonebook = phonebook
        self.answers = {
            "main_menu": ""
        }

    def build(self):
        print(MENU_TITLE)
        self.main_menu()

    def run(self):
        self.build()

    def main_menu(self):
        while self.answers["main_menu"] != "Exit":
            questions = [
                {
                    'type': 'list',
                    'name': 'main_menu',
                    'message': "How can I help you?\n",
                    'choices': ['Show contacts', 'Delete a contact', 'Add a new contact', 'Exit'],
                }
            ]
            self.answers = prompt(questions, style=custom_style_3)
            if self.answers["main_menu"] == "Show contacts":
                self.print_contacts()
            elif self.answers["main_menu"] == "Delete a contact":
                self.delete_contact_menu()
            elif self.answers["main_menu"] == "Add a new contact":
                self.add_new_contact()

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
        questions = [
            {
                'type': 'input',
                'name': 'delete_contact_id',
                'message': 'Enter ID of contact you want to delete',
                'validate': ContactExistValidator,
                'filter': lambda val: int(val)
            },
            {
                'type': 'confirm',
                'name': 'delete',
                'message': 'Are you sure you want to delete this contact?',
                'default': False

            }]
        answers = prompt(questions, style=custom_style_3)
        if answers["delete"]:
            DeleteContactService(self.phonebook, answers["delete_contact_id"]).run()

    def add_new_contact(self):
        questions = [
            {
                'type': 'input',
                'name': 'contact_name',
                'message': "Please enter contact name"
            }, {
                'type': 'input',
                'name': 'contact_surname',
                'message': "Please enter contact surname"
            }, {
                'type': 'input',
                'name': 'contact_phone_number',
                'message': "Please enter contact phone number"
            }, {
                'type': 'input',
                'name': 'contact_phone_number_type',
                'message': "Please enter contact phone number type"
            }
        ]

        answers = prompt(questions, style=custom_style_3)
        CreateContactService(answers["contact_name"],
                             answers["contact_surname"],
                             answers["contact_phone_number"],
                             answers["contact_phone_number_type"],
                             self.phonebook).run()


class ContactExistValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))
