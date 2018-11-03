this_tuple = ("apple", "banana", "grapes")
print(this_tuple) # print tuple

print(this_tuple[1]) # print item by index

#this_tuple[1] = "Carrot"
#print(this_tuple) # cannot change its value

for x in this_tuple:
    print(x)  # for loop

if "apple" in this_tuple:
    print("Yes, apple is in the list") # check if item exists

print(len(this_tuple)) # length of tuple

del this_tuple # delete tuple completely

this_tuple = tuple(("grapes", "mango", "banana"))
print(this_tuple) # construct the tuple

