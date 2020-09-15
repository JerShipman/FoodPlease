#copies from the file into a list and then returns that list.
def getFileName(listNumber):
    if listNumber == 1:
        return "outchoices.txt"
    elif listNumber == 2:
        return"inchoices.txt"
    else:
        return "error"

def copyToList(listNumber):
    lists = []
    fileName = getFileName(listNumber)
    file = open(fileName, "r")  # open correct file in read only mode
    for line in file:  # add file line by line into lists list
        lists.append(line)
    file.close()
    return lists

def saveToFile(fileNumber, newList):
    fileName = getFileName(fileNumber)
    file = open(fileName,"w")
    for x in range(len(newList)):
        print(newList[x], end='', file=file)
    file.close()

def checkForFiles():
    file = open('inchoices.txt', 'a+')
    file.close()
    file = open('outchoices.txt', 'a+')
    file.close()

    
def downloadFilesToLists():
    eatInList = []
    eatOutList = []
    checkForFiles()

    print("downloading files...")
    eatOutList = copyToList(1)
    eatInList = copyToList(2)

    print("done downloading files\n")
    return eatInList, eatOutList