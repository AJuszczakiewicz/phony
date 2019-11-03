import json
from phonebook_factory import PhonebookFactory

def read_file(file_name):
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
    return data

def main():
    json_data = read_file("phonebook.json")
    phonebook = PhonebookFactory(json_data).build()

if __name__ == "__main__":
    main()