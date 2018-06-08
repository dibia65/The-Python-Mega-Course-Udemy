# Read the content of a file and display the output containing their names and length of names

fruits = open("fruits.txt", "r")
fruitNames = fruits.read()
fruits.close()

print(fruitNames)

fruitList = fruitNames.split("\n")

for i in fruitList:
    if len(i):
        print(len(i))
