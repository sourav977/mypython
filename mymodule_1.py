# Module: A file containing a set of functions you want to include in your application.
def greeting(name):
    print("hello " + name)

# The module can also contains variables of all types (arrays, dictionaries, objects etc):
person1 = {"name":"sourav patnaik", "age":24, "location":"HYD" }

class Car(object):
    """blueprint for car"""
    def __init__(self, model="nano", color="black", company="tata", speed_limit=100):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model