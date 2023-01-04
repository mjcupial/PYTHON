from items import Note, BusinnesCard

class Organizer:
    __owner = ""
    __data_base = []

    def __init__(self, owner):
        self.owner = owner

    def AddNote(self):
        prio = input("Prio: ")
        title = input("Title: ")
        content = input("Content: ")
        new_note = Note(prio, title, content)
        self.__data_base.append(new_note)
        
    def AddBusinessCard(self):
        prio = input("Prio: ")
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        new_business_card = BusinnesCard(prio, name, surname, phone)
        self.__data_base.append(new_business_card)

    def ShowNotes(self):
        print("Notes list:\n")
        for i in self.__data_base:
            if i.type == "note":
                print(i)

    def ShowBusinessCard(self):
        print("Business Card list:\n")
        for i in self.__data_base:
            if i.type == "business card":
                print(i)