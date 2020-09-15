import fileManager
import random

dineInList = []
dineOutList = []

def pickForMe(arr):
    return int(random.choice(arr))

# print the options from the list
def displayMenu(arr):
    for i in range(len(arr)):
        if i != '' or i != ' ':
            print(str(i) + ".) " + arr[i], end='')

#adds items to list and then saves it to the file
def addToList(list2Fix, listNum):
    print("what do you want to add? Please separate with commas like")
    userInput = input()
    inputList = userInput.split(",")
    for i in range(len(inputList)):
        inputList[i] += '\n'
        list2Fix.append(inputList[i])
    fileManager.saveToFile(listNum, list2Fix)

#removes items from list and then saves the list to file
def removeFromList(list2Fix, listNum):
    print("what do you want to Remove? (seperate with space and put items in acending order)")
    displayMenu(list2Fix)
    userInput = input()
    inputList = userInput.split(" ")
    counter = 0
    for i in inputList:
        x = int(i)
        list2Fix.pop(x-counter)
        counter += 1
    fileManager.saveToFile(listNum, list2Fix)


#updates the menus
def foodUpdate(listNum):
    if listNum == 1:
        listToFix = dineOutList
    else:
        listToFix = dineInList

    print("\nAre you looking to \nA: Add\nB: Remove\nC: Go back to main menu")
    choice = input()
    if choice == "a":
        addToList(listToFix, listNum)
    elif choice == "b":
        removeFromList(listToFix, listNum)
    elif choice == 'c':
        return
    else:
        print("Invalid input")
        return

# the dine out option
def dineOut():
    print("\nDining Out")
    displayMenu(dineOutList)
    choice = input()
    selectedChoices = choice.split(" ")
    randomChosen = pickForMe(selectedChoices)
    print(dineOutList[randomChosen])
    print("Not happy, redo by typing \"r\". You can go to the main menu by typing \"m\".")
    choice = input()
    if choice == "r":
        selectedChoices.remove(str(randomChosen))
        randomChosen = pickForMe(selectedChoices)
        print(dineOutList[randomChosen])
        print("If you still aren't happy... that just means you are really picky!")
        quit()
    else:
        return


# the dine in option
def dineIn():
    print("\nDining in")
    displayMenu(dineInList)
    choice = input()
    selectedChoices = choice.split(" ")
    randomChosen = pickForMe(selectedChoices)
    print(dineInList[randomChosen])
    print("Not happy, redo by typing \"r\". You can go to the main menu by typing \"m\".")
    choice = input()
    if choice == "r":
        selectedChoices.remove(str(randomChosen))
        randomChosen = pickForMe(selectedChoices)
        print(dineInList[randomChosen])
        print("If you still aren't happy... that just means you are really picky!")
        quit()
    else:
        return

# the update menus option which will allow you to delete from the file
def updateMenus():
    print("\nUpdate Menus\nA: Dine Out options\nB: Cook Food options\nC: Go back")
    userIput = input()
    choice = userIput.lower()
    if choice == 'a':
        foodUpdate(1)
    elif choice == 'b':
        foodUpdate(2)
    elif choice == 'c':
        return

#allows user to select if they want to eat in or dine out or update menus
def selectDiningOption():
    print("\nDo you want to \nA: Dine Out\nB: Cook Food\nC: Update Menus\nD: Quit")
    userIput = input()
    choice = userIput.lower()
    if choice == 'a':
        dineOut()
        return 0
    elif choice == 'b':
        dineIn()
        return 0
    elif choice == 'c':
        updateMenus()
        return 0
    elif choice == "d":
        return 1
    else:
        return 0

if __name__ == "__main__":
    dineInList, dineOutList = fileManager.downloadFilesToLists()
    quitBool = selectDiningOption()
    while quitBool != 1: #checks to see if user is ready to quit
         quitBool = selectDiningOption()
    