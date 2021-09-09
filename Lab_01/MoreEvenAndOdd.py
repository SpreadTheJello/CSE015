numList = input("Please enter 10 numbers (seperate numbers with a space): ")
numListSplit = numList.split(" ")
finalNum = []

# Convert String list to Int list
for i in range(0, len(numListSplit)):
    numListSplit[i] = int(numListSplit[i])

# Checks if ODD, add to list
for i in range(len(numListSplit)):
    if(numListSplit[i] % 2 == 1):
        finalNum.append(numListSplit[i])

# Convert String list to Int list
for i in range(0, len(finalNum)):
    finalNum[i] = int(finalNum[i])


if(not finalNum):
    print("No odd numbers were entered.")
else:
    print(max(finalNum))

