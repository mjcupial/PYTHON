from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, type, prio):
        self.type = type
        self.prio = prio
    
    @abstractmethod
    def __str__(self):
        pass

class Note(Item):
    def __init__(self, prio, title, content):
        super().__init__("note", prio)
        self.title = title
        self.content = content
    
    def __str__(self):
        info = f"{self.type}; Priorytet: {self.prio}\n"
        info += self.title + "\n"
        info += self.content + "\n"
        return info

class BusinnesCard(Item):
    def __init__(self, prio, name, surname, phone):
        super().__init__("business card", prio)
        self.name = name
        self.surname = surname
        self.phone = phone
    
    def __str__(self):
        info = f"{self.type}; Priorytet: {self.prio}\n"
        info += f"{self.name} {self.surname}\n"
        info += f"{self.phone}\n"
        return info
