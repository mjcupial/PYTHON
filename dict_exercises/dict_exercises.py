# SOURCE:   https://www.w3resource.com/python-exercises/dictionary/

#1: Write a Python script to sort (ascending and descending) a dictionary by value
'''
itemgetter(0) sorts by index 0 in tuple (key,value), so by key --> alphabetical
itemgetter(1) sorts by index 1 in tuple (key,value), so by value --> numerical
DOCS: https://docs.python.org/3/library/operator.html

sorted: key is optional, and reverse can be True/False (default)
DOCS: https://docs.python.org/3/library/functions.html#sorted
'''
import operator
d1 = {"first": 2, "third": 4, "fourth": 3, "second": 1, "zero": 0}
print(f"origin dict: {d1}")

sorted_d_up = sorted(d1.items(), key=operator.itemgetter(1))
print(f"Ordered by values: {sorted_d_up}")

sorted_d_down = sorted(d1.items(), key=operator.itemgetter(1), reverse=True)
print(f"Ordered by values: {sorted_d_down}")


#2: Write a Python script to add a key to a dictionary
d2 = {0: 10, 1: 20}
d2.update({2: 30})
print(d2)


#3: Write a Python script to concatenate following dictionaries to create a new one. Expected results {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
https://favtutor.com/blogs/merge-dictionaries-python
'''
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50, 6:60}
print({**dict1, **dict2, **dict3})
'''
dict4 = {}
for d in (dict1, dict2, dict3): dict4.update(d)
'''


#4 Write a Python script to check whether a given key already exists in a dictionary
person = {"name": "John", "surname": "Travosky", "age": 35, "email": "jT@something.com"}

def if_key_in_dict(key):
    if key in person:
        print(f"The key {key} exists. The value is {person[key]}")
    else:
        print(f"The key {key} does not exit")

if_key_in_dict("name")
if_key_in_dict("address")


#5 Write a Python program to iterate over dictionaries using for loops

#Normal loop:
for k,v in person.items():
    print(f"{k} --> {v}")

#dict comprehension
print({
    k: f"{v} value of key" for k,v in person.items()
})