# List concept
thelist = ["apple", "orange", "banana", "cherry"] #list created
print(thelist) #ordered
# check 100 is there in list
print(100 in thelist)

temp = thelist[3]
thelist[3] = thelist[1]
thelist[1] = temp
print(thelist) #reordered and changed

thelist[0] = "guava"
print(thelist) #changable

# copy
newlist = thelist
print(newlist is thelist)
print(newlist is not thelist)
# cpoied = thelist.copy()

print(len(thelist)) #length of list

# INSERT, APPEND
thelist.append("mango") #append element at the end
print("oldlist is", thelist)
print("newlist is", newlist)

thelist.insert(2,"pineapple") # add an item at the specified index
print("edited pineapple in oldlist but newlist reflected as:", newlist)

# REMOVE
thelist.remove("guava") # removes the specified item
print("removed guava from newlist, but oldlist reflected as:", newlist)

thelist.pop() # removes the last item if index is not provided
print("oldlist :", thelist)
print("newlist :", newlist)

for item in thelist:
    if item == "orange":
        print(item)
    else:
        print("other fruit")

thelist.extend(newlist)
print("======",thelist)

# DELETE list
del thelist
print("old list deleted")
print("newlist :", newlist)

# clear list, it will empty the list
#newlist.clear()
#print(newlist)
# x = 5
# del x
# print(x)

# use the list() constructor to make a list
nlist = list((1,2,3))
print(nlist)
nlist.reverse
print(nlist)