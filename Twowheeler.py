from abc import ABC, abstractmethod

class Twowheeler:

    owner = "mj.c company"
    mileage = 0

    def __init__(self, type, brand, color):
        self.type = type
        self.color = color
        self.brand = brand
    
    def run(self):
        self.mileage += 1

    def give_mileage(self):
        print(f"mileage: {self.mileage}")

    @abstractmethod
    def giveData(self):
        pass

class bicycle(Twowheeler):
    def __init__(self, brand, color, year, speed_max):
        super().__init__("bicycle", brand, color)
        self.year = year
        self.speed_max = speed_max
    
    def giveData(self):
        data = f"""
        Super fast {self.type}: {self.speed_max} km/h
        brand | color: {self.brand} | {self.color}
        mileage: {self.mileage}
        """
        return data

class scooter(Twowheeler):
    def __init__(self, brand, color, year, style):
        super().__init__("skuter", brand, color)
        self.year = year
        self.style = style
        self.gearbox = "auto"
    
    def giveData(self):
        data = f"""
        Piękny {self.type}: {self.style}, {self.year}r.
        brand | color: {self.brand} | {self.color}
        mileage: {self.mileage}
        """
        return data

dataBase = []
dataBase.append(bicycle("Honda", "red", 1996, 232))
dataBase.append(bicycle("BMW", "black", 2015, 190))
dataBase.append(scooter("Vespa", "white", 2001, "Italian"))
dataBase.append(scooter("Junak", "beige", 2005, "Scandinavian"))
for i in dataBase:
    print(i.giveData())