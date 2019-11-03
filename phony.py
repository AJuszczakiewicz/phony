from jsonReader import JsonReader
from phoneNumber import PhoneNumber
from contact import Contact
from phonebook import Phonebook

def main():
    phonebook = JsonReader().load_data()
    phonebook.delete_contact_by_contact_id(2)
    print(phonebook)

if __name__ == "__main__":
    main()