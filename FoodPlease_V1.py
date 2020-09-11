import random

def sortArr(arr):
    return sorted(arr)


def lc(char):  # returns a lowercase
    if char == "a" or char == "A":
     
           return "a"
    elif char == "b" or char == "B":
        return "b"
    else:  # char == "c" or char == "C":
        return "c"
        

def updateMenu(char):
    if lc(char) == "a":
        x = input("Dine-Out Update\nA: Add\nB: Remove\nC: Go Back\n")
        if lc(x) == "a":
            print("This is the add option")
            addArr = input("Type what you would like to add with commas. Ie: Jamba Juice,Taco Bell\n")
            addArr1 = addArr.split(",")
            for i in range(len(addArr1)):
                print("Whats the distance for " + addArr1[i])
                distance = input("")
                addArr1[i] = addArr1[i] + " : " + str(distance) + "\n"
            saveFile(1, addArr1)

        elif lc(x) == "b":
            print("This is the remove option, not yet programmed")

        else:
            print("This is the Go back option. Its not done yet so thank Jer for that")
    else:
        x = input("Dine-in Update\nA: Add\nB: Remove\nC: Go Back\n")
        

def displayMenu(arr):
    for i in range(len(arr)):
        print(str(i) + ".) " + arr[i], end='')


def saveFile(a, arr):
    if a == 1:
        theFile = "outchoices.txt"
    else:
        theFile = "inchoices.txt"
    temparr = []
    file = open(theFile, "a")
    for x in range(len(arr)):
        print(arr[x], end='', file=file)
    file.close()
    file = open(theFile, "r")
    for line in file:
        temparr.append(line)
    file.close()
    arr1 = sortArr(temparr)
    file = open(theFile, "w+")
    for x in range(len(arr1)):
        print(arr1[x], end='', file=file)
    file.close()


def pickForMe(arr):
    return int(random.choice(arr))


def eatLocation(num):
    if num == 1:
        fileName = "outchoices.txt"
    else:
        fileName = "inchoices.txt"
    arr = []
    file = open(fileName, "r")  # open correct file
    print("Type in the numbers you think sound good, separate with a space. Ie: 1 3 8 9"
          "\nPut in extra votes for food you really want\n")
    for line in file:  # add file line by line into array arr
        arr.append(line)
    displayMenu(arr)  # run array through forloop and display options
    file.close()
    selectedChoices = input().split(" ")
    return arr, selectedChoices


def eatWhere():
    option = input("Are you looking to eat-out or are you looking to cook?\n"
                   "A: Eat-out\n"
                   "B: Cook\n"
                   "C: Update Menus\n")
    if lc(option) == "a":
        arr, selc = eatLocation(1)
        return arr, len(arr), selc
    elif lc(option) == "b":
        arr, selc = eatLocation(2)
        return arr, len(arr), selc
    elif lc(option) == "c":
        xarr = input("Update\nA: Dine-Out Options\nB: Dine-In Options\nC: Go Back\n")
        if lc(xarr) == "c":
            return 0, -1, 0
        else:
            updateMenu(xarr)
            return 0, -1, 0
    else:
        print("Option is not valid, Please try again")
        eatWhere()

##################################
##########main####################
arr = 0
lengOfArr = 0
selc = 0
arr, lengOfArr, selc = eatWhere()
if lengOfArr == -1:
    while lengOfArr == -1:
        arr, lengOfArr, selc = eatWhere()

if lengOfArr != 0:
    x = pickForMe(selc)
    print("The choice has been chosen:\n" + str(arr[x]))
