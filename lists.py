this_list = ["apple", "Banana", "orange"]

print(this_list) # print this_list

print (this_list[1]) # access item

this_list[1] = "blackforest"
print(this_list) # change item value

for x in this_list:
    print(x) # for loop

if "apple" in this_list:
    print("Yes, Apple is in this_list") # check if item exist

print(len(this_list)) # list length

this_list.append("grapes")
print(this_list) #append

this_list.insert(1, "Watermilon")
print (this_list) # add item at specified index

this_list.remove("blackforest")
print(this_list) # remove item

this_list.pop(1)
print(this_list) # remove specified index

del this_list[0]
print(this_list) # remove specified index

this_list = list(("Apple", "Banana", "Grapes"))
print(this_list) # construct list

this_list.reverse()
print(this_list) # reverse list

this_list.sort()
print(this_list) # sort the list

this_list.clear()
print(this_list) #empty the list

del this_list
print(this_list) # delete list completely
