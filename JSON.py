""" JSON is a syntax for storing and exchanging data
JSON is text written with java script object notation.
Python has a builtin  package JSON  which can be use to work with json data
"""

import json

x = '{"fruit" : "apple", "color": "red", "flavour": "sweet"}'

y = json.loads(x)
print(y["color"])



