thislist = ["apple", "Banana", "orange"]

print(thislist)

print (thislist[1])

thislist[1] = "blackforest"

print(thislist)

for x in thislist:
    print(x)

if "apple" in thislist:
    print("Yes, Apple is in thislist")

print(len(thislist))

thislist.append("grapes")
print(thislist)