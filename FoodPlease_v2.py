import fileManager
import random

dineInList = []
dineOutList = []

def pickForMe(arr):
    return int(random.choice(arr))

#print the options from the list
def displayMenu(arr):
    for i in range(len(arr)):
        print(str(i) + ".) " + arr[i], end='')

#the dine out option
def dineOut():
    print("\nDining Out")
    displayMenu(dineOutList)
    print("To go back type \"back\"")
    choice = input()
    goBack(choice)
    selectedChoices = choice.split(" ")
    randomChosen = pickForMe(selectedChoices)
    print (dineOutList[randomChosen])
    print ("Not happy, redo by typing \"r\". You can go to the main menu by typing \"m\". Or if you are happy type \"q\"")
    choice = input()
    if choice == "r":
        selectedChoices.remove(str(randomChosen))
        randomChosen = pickForMe(selectedChoices)
        print (dineOutList[randomChosen])
        print ("If you still aren't happy... that just means you are really picky!")
    elif choice == "m":
        selectDiningOption()
    else:
        return


#the dine in option
def dineIn():
    print("\nShe's a cooking queen")
    displayMenu(dineInList)
    print("To go back type \"back\"")
    choice = input()
    goBack(choice)

#the update menus option which will allow you to delete from the file
def updateMenus():
    print("\nUpdate Menus\nA: Dine Out options\nB: Cook Food options\nTo go back type \"back\"")
    userIput = input() 
    choice = userIput.lower()
    if choice == 'a':
        #dineInUpdate()
        print("a")
    elif choice == 'b':
        #dineOutUpdate()
        print("b")
    else:
        print("c")
        #selectDiningOption()
  
#this fucntion allows the user to select if they want to eat out or cook
def selectDiningOption():
    print("Do you want to \nA: Dine Out\nB: Cook Food\nC: Update Menus")
    userIput = input() 
    choice = userIput.lower()
    if choice == 'a':
        dineOut()
    elif choice == 'b':
        dineIn()
    elif choice == 'c':
        updateMenus()
    elif choice == "quit":
        return
    else:
        print("\nNot valid, select again!\n")
        selectDiningOption()

#checks to see if user typed back and will call selectDiningOption
def goBack(choice):
    if choice == "back":
        selectDiningOption()
    else:
        return
    

if __name__ == "__main__":
    dineInList, dineOutList = fileManager.downloadFilesToLists()
    selectDiningOption()
   
    
    