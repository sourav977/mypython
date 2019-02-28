# for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x, end=' ')

for x in "sourav":
  if x == 'o':
      continue
  if x == 'a':
      break # exit loop
  print(x)

for x in range(30,35): #by default it increments by 1
      print(x)
      x +=1

for z in range(10,20,2): # third parameter is inc value
    print(z)

# "else" in for loop
for x in range(6): # from 0 to 5
      print(x)
else:
  print("Finally finished!")

# nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)