# Arrays are used to store multiple values in one single variable.
# Python does not have built-in support for Arrays, but Python "lists" can be used instead.
cars = ["Ford", "Volvo", "BMW",123,23.90]
# print(cars)
# print(cars[0])
print(cars[2]) 
# print(cars[5]) # IndexError: list index out of range

# looping
for item in cars:
    print(item)

# length of array
print(len(cars))

# adding array element
cars.append("Honda")
print(cars[4:])

# pop() to remove an element from array
print(cars)
cars.pop(1) # remove [1] index item
print(cars)

# remove() an element
cars.remove(23.90)
print(cars)

# reverse a array
cars.reverse()
print(cars) #now the original array will look like this

x = cars.index("BMW")
print(x)

# count the number of occurance of element
cnt = cars.count(123)
print(cnt)

num = [1,2,3,4,5]
print(num)
num.reverse()
print(num)