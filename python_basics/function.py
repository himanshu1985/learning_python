def my_function():
    print("Hello, this is my first function")


my_function()  # calling function


def my_function(fname):
    print(fname + "Smart")


my_function("Himanshu ")
my_function("Pandit ")
my_function("Rajesh ")  # Information can be passed to functions as parameter


def my_function(country="Norway"):
    print("I am from " + country)


my_function("India")
my_function("England")
my_function()
my_function("Pakistan")  # If we call the function without parameter, it uses the default value


def my_function(x):
    return 5*x


print(my_function(3))
print(my_function(5))
print(my_function(6))  # function return a value, use the return statement








