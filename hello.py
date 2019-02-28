print ("hello")
print('hello')
if 5>3:
  print('success')

x = 10
y = 'sourav'
print(x,y)
print(type(x))
print(type(y))
print('hello    '+ y)
# error print(x + y)

print(x+100)

x = 35e3
y = 12E4
z = -87.7e100

print(x, type(x))
print(y, type(y))
print(z, type(z))

x = 3+5j
y = 5j
z = -5j

print(x, type(x))
print(y, type(y))
print(z, type(z))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
# z = int("3e3") # invalid literal for int() with base 10: '3e3'
z = float("32e4")
print(x, type(x))
print(y, type(y))
print(z, type(z))