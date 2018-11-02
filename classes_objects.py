class User(object):
    def __init__(self, something):
        print("user init called")
        self.something = something

    def method(self):
        return self.something

class Student(User):
    def __init__(self, something):
        User.__init__(self, something)
        print("Student init called")
        self.something = something

    def method(self):
        return self.something


my_object = Student("Himanshu")  # init function


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("Hello my name is: " + self.name, "My age is: ",  self.age)


p1 = person("Himanshu", 36)
p1.age = 40

p1.my_func()  # init function






