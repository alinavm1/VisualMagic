# what makes it list is using[ ] 
myList = [1,5,5,5,7,1]
# here you say: "THIS is my list"
myList = list([1,3,12,1,1,5,1])

for element in myList:
    print(element)
    pass

listLengh = len(myList)

print("Second Attempt")

for iteration in range (0,listLengh):
    print("Index:{0} Value: {1}". format (myList[iteration]))


firstValue = 2
secondValue = -5


# Equality Operation
print(firstValue == secondValue)

# Less than Operator
print(firstValue < secondValue)

# Greater than operator
print (firstValue > secondValue)
