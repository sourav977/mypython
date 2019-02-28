# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# syntax:  lambda arguments : expression
# The expression is executed and the result is returned.

x = lambda a : a + 10
print(x(100*2))

result = lambda a,b,c : (a + b) / c
print(result(10,30,3))

# anonymous function inside another function
def myfunc(n):
  return lambda a : {(a * n ** 2)/432}

val = myfunc(200)
print(val(20))