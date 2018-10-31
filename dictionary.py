this_dict = {"lion" : "tiger",  "brand" : "animal", "legs" : "four"}
print(this_dict)

x = this_dict["lion"]
print(x) # Get the value of the "lion" key

x = this_dict.get("lion")
print(x) # Get the value of the "lion" key

this_dict["brand"] = "bird"
print(this_dict) # Change the "brand" to bird

for x in this_dict:
    print(x) # loop through a dictionary by using a for loop, the return value are the keys of the dictionary

for x in this_dict:
    print(this_dict[x]) # Print all values in the dictionary, one by one

for x in this_dict.values():
    print(x) # the values() function to return values of a dictionary

for x , y in this_dict.items():
    print(x, y) # Loop through both keys and values, by using the items() function

if "lion" in this_dict:
    print("Yes, lion is one of the keys in the this_list dictionary") # Check if "lion" is present in the dictionary

print(len(this_dict)) # To determine how many items

this_dict["legs"] = "Eight"
print(this_dict) # Adding an item to the dictionary

this_dict.pop("brand")
print(this_dict) # removes the item with the specified key name

this_dict.popitem()
print(this_dict) # removes the last inserted item

this_dict =	dict(brand="Ford", model="Mustang", year=1964)
print(this_dict) # constructor to make a dictionary

this_dict.clear()
print(this_dict) # The clear() keyword empties the dictionary

del this_dict["brand"]
print(this_dict) # removes the item with the specified key name

del this_dict
print(this_dict) # delete the dictionary completely