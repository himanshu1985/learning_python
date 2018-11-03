""" JSON is a syntax for storing and exchanging data
JSON is text written with java script object notation.
Python has a builtin  package JSON  which can be use to work with json data
"""

import json

x = '{"fruit" : "apple", "color": "red", "flavour": "sweet"}'
y = json.loads(x)  # If you have a JSON string, you can parse it by using the json.loads() method
print(y["color"])


x = {"fruit": "apple", "color": "red", "flavour": "sweet"}
y = json.dumps(x)  # If you have a Python object, you can convert it into a JSON string by using the json.dumps() method
print(y)


print(json.dumps(["name", "rahim", "color"]))
print(json.dumps({"name": "himanshu", "age": 24, "school": "army"}))
print(json.dumps(("name", "himanshu", "nidhi")))
print(json.dumps(24))
print(json.dumps(2.45))
print(json.dumps("himanshu"))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


x = {
    "name": "Himanshu",
    "Age": 36,
    "School": "Army",
    "Married": "True",
    "Children": "Yashvi",
    "pets": None,
    "cars": [
        {"model": "BMW 250", "mpg": 85},
        {"model": "Marti", "mpg": 65}
    ]
}

print(json.dumps(x, indent=4, separators=(". ", "= "), sort_keys= True))
