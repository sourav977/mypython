# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


# a function is defined using "def"

def myfunction():    # function defination
    print("hello")   # function body
    for x in range(50,100,10):
        if x == 70:
            continue
        print(x)
        if x == 90:
            break

myfunction()  # calling a function

# function with parameter
def addition(a,b):
    #print("result :",a+b)
    return (a+b)

print(addition("hi","bye"))
print(addition(30,90))
rslt = addition(200,500)
print(rslt)
#addition(20,"hello")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
