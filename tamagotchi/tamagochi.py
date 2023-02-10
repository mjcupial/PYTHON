import random
from random import randint

class Animal:
    water_in_bowl = 100
    food_in_bowl = 100
    poop = 0

    def __init__(self, name, age, is_predator):
        self.name = name
        self.age = age
        self.is_predator = is_predator

    def __repr__(self):
        if self.is_predator == True:
            info = "I like meat."
        else:
            info = "I prefer plant products."
        return f"Hi! I'm {self.name}, {self.age}. {info}"

    def drink_water(self):
        how_much = randint(5, 62)
        Animal.water_in_bowl -= how_much
        if Animal.water_in_bowl > 0:
            print(f"Yammy! water in bowl: {Animal.water_in_bowl}%")
        else:
            print("I can't drink, there is no enough water!")

    def eat(self):
        how_much = randint(5, 12)
        Animal.food_in_bowl -= how_much
        is_poop = random.choice([False, True])
        if is_poop == True:
            how_much = randint(1,10)
            Animal.poop += how_much
        if Animal.food_in_bowl > 0:
            print(f"Delicious! food in bowl: {Animal.food_in_bowl}%")
        else:
            print("I can't eat, there is no enough portion!")



    def add_water(self):
        how_much = randint(5, 68)
        Animal.water_in_bowl += how_much
        if Animal.water_in_bowl > 0 and Animal.water_in_bowl < 100:
            print(f"Water added. Now in bowl: {Animal.water_in_bowl}%")
        if Animal.water_in_bowl >= 100:
            Animal.water_in_bowl = 100
            print(f"I CAN'T ADD MORE WATER THE BOWL IS FULL")

class Cat(Animal):
    happiness = 20
    litter_box = 0
    def __init__(self, name, age, toy):
        super().__init__(name, age, is_predator=True)
        self.toy = toy

    def play(self, toy):
        happy_level = randint(1, 27)
        if toy == True:
            Cat.happiness += happy_level
            if Cat.happiness >= 100:
                Cat.happiness = 100
                print(f"Maximum level of happiness achieved!")
        else:
            Cat.happiness -= happy_level
            if Cat.happiness <= 10:
                Cat.happiness = 10
                print(f"Your animal is not happy...")
        print(f"happiness level: {Cat.happiness}%")


    def check_litter_box(self):
        return self.poop



# class Mouse(Animal, Cat):
#     def __init__(self, name, age, toy, is_kuweta_clear):
#         super().__init__(name, age, is_predator=True)
#         self.toy = toy
#         self.is_kuweta_clear = is_kuweta_clear






# animal = Animal("Piesel", "4", True)
# print(animal)
# animal.drink_water()
# animal.drink_water()
# print(Animal.water_in_bowl)
# animal.add()
#############################################################
cat = Cat("Kicia", "8", True)
print(cat)
cat.eat()
print(cat.poop)

cat.eat()
print(cat.poop)

cat.eat()
print(cat.poop)

cat.eat()
print(cat.poop)





