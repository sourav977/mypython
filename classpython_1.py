class Car:
    """blueprint for car"""
    def __init__(self, model="nano", color="black", company="tata", speed_limit=100):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
# "__init__" is a reseved method in python classes.
# It is known as a constructor in object oriented concepts.
# This method called when an object is created from the class
# and it allow the class to initialize the attributes of a class
newcar = Car() # creating object of a class, The procedure to create an object is similar to a function call.
print(newcar)
maruthi_suzuki = Car("ertiga", "black", "suzuki", 60) # these arguments will pass to "__init__" method  to initialize the object
audi = Car("A6", "red", "audi")
print(maruthi_suzuki.color)
print(maruthi_suzuki.company)
print(maruthi_suzuki.speed_limit)
print(maruthi_suzuki.model)
print(maruthi_suzuki.__doc__)
print(audi.speed_limit)

class Rectangle:
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    def get_area(self):
        return self.length * self.breadth
    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost
# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000)
# whenever an object calls its method, the object itself is passed as the first argument.
# so r.get_area() will convert as Rectangle.get_area(r)
print("Area of Rectangle: %s cm^2" % (r.get_area()))
print("Cost of rectangular field: Rs. %s " %(r.calculate_cost()))


class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()