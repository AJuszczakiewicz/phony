from jsonReader import JsonReader
from phoneNumber import PhoneNumber
from contact import Contact

def main():
    number = PhoneNumber(980378343, "mobile")
    contact = Contact("Kitty", "Good Kitty")
    contact.add_new_number(number.phone_number, number.phone_type)
    print(contact)

if __name__ == "__main__":
    main()