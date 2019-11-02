class PhoneNumber:
    def __init__(self, phone_number, phone_type):
        self.phone_number = phone_number
        self.phone_type = phone_type

    def __str__(self):
        return f'\tphone number: {self.phone_number}\n\ttype: {self.phone_type}'