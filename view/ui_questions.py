from PyInquirer import Validator, ValidationError


class ContactExistValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))


main_menu = [
    {
        'type': 'list',
        'name': 'main_menu',
        'message': "How can I help you?\n",
        'choices': ['Show contacts',
                    'Delete a contact',
                    'Add a new contact',
                    'Save to file',
                    'Exit'],
    }
]

add_contact_menu = [
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

delete_contact_menu = [
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
