from logic import TruthTable

checkList = []
userInput = input("Enter your expression: ")
myTable = TruthTable([userInput])

print("")
myTable.display()

a = myTable.table

for x in a:
    checkList.append(x[1][0])

tableLength = len(checkList)

def contingency(tableLength, checkList):
    check = False
    for i in range(tableLength):
        if(checkList[(tableLength - i) - 1] != checkList[i]):
            check = True
            break
    return(check)

def tautology(tableLength, checkList):
    c = 0
    check = False
    for i in range(tableLength):
        if(checkList[i] == 1):
            c = c + 1
    if c == tableLength:
        check = True
    return(check)

def contradiction(tableLength, checkList):
    c = 0
    check = False
    for i in range(tableLength):
        if(checkList[i] == 0):
            c = c + 1
    if c == tableLength:
        check = True
    return(check)

if(contingency(tableLength, checkList) == True):
    print("\nContingency")

elif(tautology(tableLength, checkList) == True):
    print("\nTautology")

elif(contradiction(tableLength, checkList) == True):
    print("\nContradiction")

else:
    print("\ncould not solve. Invalid.")