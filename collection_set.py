# A "set" is a collection which is unordered and unindexed

# Create a Set
thisset = {"apple", "banana", 200, "car", 90.12}

# Sets are unordered, so the items will appear in a random order.
print(thisset)  # set([200, 'car', 'apple', 90.12, 'banana'])

# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
#element = thisset[0] # TypeError: 'set' object does not support indexing

for item in thisset:
    print(item)

# check "banana" is there in set
print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.
# thisset[0] = 500
# print(thisset)  # TypeError: 'set' object does not support item assignment

# add element to set using add()
thisset.add("orange")
print(thisset)

# To add more than one item to a set use the update() method.
# thisset.update(600, "pineapple", 23.56) # TypeError: 'int' object is not iterable
thisset.update(["pineapple", "guava"])
print(thisset)

# length
print(len(thisset))

# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove(200)
print(thisset)

thisset.discard(90.12)
print(thisset)

# remove last item using pop()
thisset.pop()
print(thisset)

# clear() emptys the set
thisset.clear()
print(thisset)

# delete the set
del thisset
#print(thisset)

# set() to create set
newset = set((900,800,700,600,"apple"))
print(newset)

copied = newset.copy()
print(copied)