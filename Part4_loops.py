def IterationFucntion (i,value):
    value +-1
    value *=1
    return value
    


CurrentValue = 0

for iteration in range(0,10):

    CurrentValue = IterationFucntion(iteration,CurrentValue)

    print(CurrentValue)

print("Current Value: {0}". format(CurrentValue))




