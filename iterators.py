tuple = ("apple", "banana", "orange")
my_it = iter(tuple)

print(next(my_it))
print(next(my_it))
print(next(my_it))  # Return a iterator from a tuple

mystr = "Himanshu"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))  # Strings are also iterable objects, containing a sequence of characters




class My_desk:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x

        else:
            raise StopIteration


myclass = My_desk()
myname = iter(myclass)

print(myname.__next__())

