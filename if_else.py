a = 33
b = 13
if a > b:
    print("a is greater than b")  # if else condition

a = 33
b = 33
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")  # if the previous conditions were not true, then try this condition

a = 3
b = 33
if b > a: print("b is greater than a")
elif a == b: print("a is equal to b")
else: print("a is greater than b")  # if elif else condition

print("A") if a > b else print("=") if a == b else print("B")  # all if else command in one line

a = 10
b = 20
c = 33
if a < b and c > b:
    print("Both conditions are true") # and operator

a = 10
b = 20
c = 33
if a < b or c > b:
    print("Both conditions are true")  # or operator

