# tuple declare
thistuple = ("apple", "banana", "cherry", 123)
print("tuple :", thistuple)

#member access
print(thistuple[1])

# change tuple element
#thistuple[2] = "pineapple"
#print(thistuple)

# loop through tuple
for item in thistuple:
    if item == "banana":
        print("true")
    else:
        print("other fruit")

# tuple length
print(len(thistuple))

# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#thistuple[3] = "orange" # This will raise an error
#print(thistuple)

# You cannot remove items in a tuple.
# The "del" keyword can delete the tuple completely.
del thistuple
# print(thistuple) #NameError: name 'thistuple' is not defined

# use the tuple() constructor to make a tuple
newtuple = tuple((100,200,300,400,500,100,"apple",27.12))
print(newtuple)
#check "apple" is therein this tuple
print("apple" in newtuple)
print(1000 in newtuple)

# "count" Returns the number of times a specified value occurs in a tuple
cnt = newtuple.count(100)
print(cnt)

# "index" Searches the tuple for a specified value and returns the position of where it was found
indx = newtuple.index(400)
print(indx)