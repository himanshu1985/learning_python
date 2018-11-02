import template as sir
import platform
sir.greeting("Himanshu")

a = sir.person["designation"]
print(a)

x = platform.system()
print(x) # builtin function

x = dir(platform)
print(x) # builtin function

from template import person

print(person["designation"])  #You can choose to import only parts from a module, by using the from keyword.






