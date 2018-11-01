for x in "banana":
  print(x)

fruits = ["apple", "banana", "mango"]
for x in fruits:
    print(x)
    if x == "banana":
        break  # break statement we can stop the loop before it has looped through all the items

fruits = ["apple", "banana", "mango"]
for x in fruits:
    if x == "banana":
        break
    print("break", x) # Exit the loop when x is "banana", but this time the break comes before the print

fruits = ["apple", "banana", "mango"]
for x in fruits:
    if x == "banana":
        continue
    print("continue", x) # stop the current iteration of the loop, and continue with the next

for x in range(2, 30, 3):
    print("range", x) # Increment the sequence with 3 (default is 1)

for x in range(6):
    print("processing", x)
else:
    print("Finally, Finished") # Print all numbers from 0 to 5, and print a message when the loop has ended

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "orange"]
for x in adj:
    for y in fruits:
        print(y, x)  # A nested loop is a loop inside a loop, Print each adjective for every fruit


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result


print('\n\nRecursion is used now ')
tri_recursion(6)


# Recursion is a common mathematical and programming concept. It means that a function calls itself



