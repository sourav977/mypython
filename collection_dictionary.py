# A dictionary is a collection which is unordered, changeable and indexed
# dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
    "name": "sourav",
    "age": 24,
    "year": 2018,
}
print(thisdict)

# access the items of a dictionary by referring to its key name
print(thisdict["age"])
print(thisdict.get("name"))

# can change the vale of a key
thisdict["name"] = "sikan"
print(thisdict)

#loop
for item in thisdict:
    print(item)  # returns keys

for item in thisdict:
    print(thisdict[item])   # return values

# You can also use the  values()  function to return values of a dictionary:
for item in thisdict.values():
  print(item)

# Loop through both keys and values, by using the items() function:
for key,val in thisdict.items():
    print(key,val)

# dictionary length
print(len(thisdict))

# add item to dictionary
thisdict["location"] = "bbsr"
print(thisdict)

# remove item
del thisdict["age"]
print(thisdict)

# pop()
thisdict.pop("location")
print(thisdict)

thisdict.popitem()
print(thisdict)

# clear() emptys the dictionary
thisdict.clear()
print(thisdict)

# remove dictionary completely
del thisdict
#print(thisdict) # NameError: name 'thisdict' is not defined

# use the dict() constructor to make a dictionary.
newdict = dict(name= "sourav", age= 24, place="bbsr")
print(newdict)

copied = newdict.copy()
print(copied)