from jsonReader import JsonReader
from phoneNumber import PhoneNumber
from contact import Contact
from phonebook import Phonebook

def main():
    phonebook = JsonReader().load_data()
    print(phonebook)

if __name__ == "__main__":
    main()