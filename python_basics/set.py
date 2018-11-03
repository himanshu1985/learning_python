this_set = {"apple", "grapes", "banana"}
print(this_set) # print set

for x in this_set:
    print(x)  #loop

if "apple" in this_set:
    print("Yes, apple is in the list") # condition

print("apple" in this_set) # check if apple present in this set

this_set.add("orange")
print(this_set) # add item

this_set.update(["mango", "watermilon"])
print(this_set) # add

print(len(this_set)) #number of items

this_set.remove("watermilon")
print(this_set) # remove item

this_set.discard("apple")
print(this_set) # remove item

x = this_set.pop()
print(x)
print(this_set) # Sets are unordered, so when using the pop() method, you will not know which item that gets removed

this_set = set(("apple", "grapes", "banana"))
print(this_set) # the set() constructor to make a set

this_set.clear()
print(this_set) # The clear() method empties the set

del this_set
print(this_set) # The del keyword will delete the set completely

this_set = set("apple", "grapes", "banana")
print(this_set)