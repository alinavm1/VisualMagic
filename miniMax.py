def minMax(inputList):
    minValue =0
    maxValue =0
    listLenght = len(inputList)
    for iteration in range(0,listLenght):
            value = inputList [iteration] 
            if iteration ==0:
                minValue = value 
                maxValue = value
            
            else:
                if value > maxValue:
                    maxValue = value
                elif value < maxValue:
                    minValue = value
       

    return minValue,maxValue

myList = list([1,4,6,7,7,-1,-12,18])

minMaxValues = minMax(myList)

print("MinValue: {0} MaxValue {1}".format(minMaxValues[0],minMaxValues[1]))


