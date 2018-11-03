try:
    print(x)
except:
    print("Error Occured")


try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


try:
    print(x)
except:
    print("Variable x is not defined")
finally:
    print("Something else went wrong")


