class ComplexNumber:
    def __init__(self,r = 0,i = 0, anonymous = "hi"):
        self.real = r
        self.imag = i
        self.anonymous = anonymous

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))
    
    def anyfunc(self):
        print(self.anonymous)

# Create a new ComplexNumber object
c1 = ComplexNumber(10,3)
# print(c1)
# Call getData() function
# Output: 2+3j
c1.getData()
c1.anyfunc()

# Create another ComplexNumber object
c2 = ComplexNumber(5)
c2.getData()
c2.attr = 10 # create a new attribute 'attr' for c2 object
# attributes of an object can be created on the fly

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
# print(c1.attr)

# Any attribute of an object can be deleted anytime, using the "del" statement.
del c1.anonymous
c2.anyfunc() # hi
c1.anyfunc() # # AttributeError: 'ComplexNumber' object has no attribute 'anonymous'
c1.getData()

# deleting object itself
del c1
del c2