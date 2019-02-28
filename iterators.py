# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Lists, tuples, dictionaries, and sets are all iterable objects
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# We can also use a for loop to iterate through an iterable object:
for x in mytuple:
  print(x)

# To create an object/class as an iterator we have to implement 
# the methods __iter__() and __next__() to your object.
class myclass:
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        x = self.num
        self.num += 1
        return x

mc = myclass()
myiter = iter(mc)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))