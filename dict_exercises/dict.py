from functools import total_ordering
from random import random
from unicodedata import name


engineer = {
    "name": "Maciej",
    "surname": "Cupial",
    "email": "maciej.cupial@nokia.com",
    "age": 31,
    "Pz1": False,
    "Pz2": True
}

engineer_2 = dict(
    name="John",
    surname="Wasky",
    email="ab@c.com",
    age=22,
    Pz1=False,
    Pz2=True
)

print(engineer["name"])
print(engineer_2["name"])

def introducing(name, surname):
    print(f"Hej {name} {surname}, nice to meet you!")

introducing(engineer["name"], engineer["surname"])

for value in engineer.values():
    print(value)
print("\n")
for key in engineer.keys():
    print(key)
print("\n")
for item in engineer.items():
    print(item)
print("\n")

print(engineer.values())
print(engineer_2.keys())
print(engineer.items())

donation = dict(
    sam=25.0,
    lena=88.99,
    chuck=13.0,
    linus=99.5,
    stan=150.0,
)
total_donations = 0
for value in donation.values():
    total_donations += value
print(total_donations)

#ask about key
print("\n\nVALUE EXISTS IN DICT")
print("adress" in engineer)

#ask about value
print("Maciej" in engineer.values())

#   $$ METHODS $$
print("\n\nMETHODS: clear, copy, fromkeys, get, pop, popitem, update")
d = dict(a=1, b=2, c=3)
print(d.clear())

d = dict(a=1, b=2, c=3)
c = d.copy()
print(d)
print(c)
print(c is d)

#new and temporary dict:
print({}.fromkeys(["a", "b", "c"], "unknown"))
print({}.fromkeys("phone", "unknown"))
print({}.fromkeys(["phone"], "unknown"))

print(engineer.get("name"))
print(engineer.get("adress"))

engineer_2.pop("age")
print(engineer_2)

print(engineer_2.popitem())
print(engineer_2)

list1 = ["CA", "NJ", "RI", "d"]
list2 = ["California", "New Jersey", "Rhode Island"]
print(
    dict(zip(list1, list2))
)

engineer_2["name"] = "NOT YOUR BUSINESS"
print(engineer_2)
engineer_2.update([("have_bike",True), ("have_car", False)])
print(engineer_2)

inventory = {"crosaint": 19, "bagel": 4, "muffin": 8, "cake": 1}
stock_list = inventory.copy()
stock_list.update([("cookie", 18)])
stock_list.pop("cake")
print(stock_list)

#dict playlist
print("\n\nDICT PLAYLIST")
playlist = {
    "title": "my playlist",
    "author": "mjc",
    "song": [
        {"title": "s1", "artists": ["JLO", "Martyniuk"], "duration": 2.50},
        {"title": "s2", "artists": "Stan Borys", "duration": 3.45},
        {"title": "s3", "artists": "Metallica", "duration": 6.45}
    ]
}

print(playlist["song"][2])

#dict comprehension
print("\n\nDICT COMPREHENSION")
nums = dict(jeden= 1, dwa= 2, trzy= 3, cztery= 4, piec= 5)
print({
   k : v**2 for k,v in nums.items()
})
print({
   k for k in nums.keys()
})
print({
   (v**3)+(2.6) for v in nums.values()
})

num_list = [1,2,3,4,5]
print({num:("even" if num%2==0 else "odd") for num in num_list})

#


