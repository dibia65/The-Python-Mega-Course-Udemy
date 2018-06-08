# Program to calculate length of a string

myString = input("Enter a string: ")

#isinstance() is a method used to compare the data type of the object passed to it. if matched it returns true else false as shown below.

if isinstance(myString, int) == True:
    print("Integers don't have length")
elif isinstance(myString, float) == True:
    print("Floats don't have length")
else:
    print("Length = %d" %(len(myString)))
