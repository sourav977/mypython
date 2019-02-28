# Class is a set or category of things having some property or 
# attribute in common and differentiated from others by kind, type, or quality.
# A Class is like an object constructor, or a "blueprint" for creating objects.
# To create a class, use the keyword class:

# As soon as we define a class, a new class object is created with the same name. 
# This class object allows us to access the different attributes as well as to 
# instantiate new objects of that class.

# we can create many objects from a class. 
# An object is also called an instance of a class and 
# the process of creating this object is called instantiation.

# All classes have a function called __init__()
# which is always executed when the class is being initiated.

class Employee: # simple class
    name = 'sourav'
    age = 24
    native = 'bbsr'

class MyClass: # class with method
    "This is a demo class"
    a = 10
    name = "sikan"
    # self represents the instance of the class. 
    # By using the "self" keyword we can access the attributes 
    # and methods of the class in python.
    # The self parameter is a reference to the class instance itself.
    def myfunction(self):
        print('Hello')

e1 = Employee() 
# creating an object of a class, 
# also called instantiation,The procedure to create an object is similar to a function call.
# whenever an object calls its method, the object itself is passed as the first argument.
print(e1)        # o/p:  <__main__.Employee instance at 0x0000000001162808>
print(e1.native) # o/p: bbsr

# without creating any object, using the default object, i.e using the class name itself
print(MyClass.a) # Output: 10

print(MyClass.myfunction) # Output: <unbound method MyClass.myfunction>
m = MyClass()
m.myfunction()

print(MyClass.__doc__) # Output: 'This is a demo class'