import json

from lib.phonebook_factory import PhonebookFactory
from view.ui import UI


def read_file(file_name):
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
    return data

def main():
    json_data = read_file("data/phonebook.json")
    phonebook = PhonebookFactory(json_data).build()
    ui = UI(phonebook).run()

if __name__ == "__main__":
    main()