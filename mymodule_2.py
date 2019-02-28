import mymodule_1 # you can also import with alias, # import mymodule_1 as m

mymodule_1.greeting("sourav") # import greeting function
print(mymodule_1.person1["age"]) # import variables

m = mymodule_1 # shortcut
m.greeting("Hyderabad")

print(m.person1)

# access exported class
newcar = m.Car("elite i20","red","hyundai",100)
print(newcar.__doc__)
print(newcar.model)

# dir() built-in function to list all the function names (or variable names) in a module
x = dir(mymodule_1)
print(x)
# imported built-in module
import platform
x = platform.system()
print(x)