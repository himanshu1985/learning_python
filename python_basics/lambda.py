x = lambda a: a + 15
print(x(5))

x = lambda a, b: a*b
print(x(5, 6))

x = lambda a, b, c: a+b+c
print(x(5, 10, 8))


def my_function(n):
    return lambda a: a*n


mydoubt = my_function(2)
mytripler= my_function(3)
print(mydoubt(5))
print(mytripler(6))  # Use that function definition to make a function that always doubles the number you send in





