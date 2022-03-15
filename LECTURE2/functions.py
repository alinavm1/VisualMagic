if __name__ != "__main__":
    from .constants import VARIABLEONE, VARIABLETW0
else:
    from constants import VARIABLEONE, VARIABLETW0

def FunctionA():
    print ("Running Function A")

def FunctionB(A,B):
    print("A: {0} B: {1}".format(A,B))


# RUN THIS CODE ONLY IF WE PRESS RUN FOR THIS FILE
if __name__ == "__main__":
    FunctionA()
