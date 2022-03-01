#Function for adding two value together, Prints and returns result
def AdditionFunction(A,B):
    result = A+B 
    print(result)
    return result 

#Print the current value to the console
def PrintCurrentValue():
    print(CurrentValue)

#Variable for keeping track of the current value
CurrentValue = 0

CurrentValue = AdditionFunction(CurrentValue,3)
CurrentValue = AdditionFunction(CurrentValue,1)
CurrentValue = AdditionFunction(CurrentValue,7)

PrintCurrentValue()

print ("use IDLE with Dark theme")
