import os
clear = lambda: os.system('cls')

def main():
    clear()
    print("INVENTORY MANAGEMENT")
    print("--------------------")
    print()
    print("Available Options:")
    print()
    print("1 - Add Items To Inventory")
    print("2 - View Inventory")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            addItemToInventory()
            break
        elif userChoice == '2':
            viewInventory()
            break

def addItemToInventory():
    clear()
    print("ADD ITEMS TO INVENTORY")
    print("----------------------")
    print()
    print("Available Options:")
    print()
    print("1 - Add multiple items")
    print("2 - Add single item")
    print()
    while True:
        userChoice = input("Choose an option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        print()
        while True:
            numItems = input("Enter the number of items to be added: ")
            if numItems.isdigit():
                break
        numItems = int(numItems)
        userItems = {}
        for i in range(1, numItems+1):
            while True:
                print()
                user_item = input("Item Name: ")
                if user_item != '':
                    break
            while True:
                item_amount = input("Item Amount: ")
                if item_amount.isdigit():
                    break
            userItems.update({user_item: int(item_amount)})

        addItemsToFile(userItems, clear=False)
        returnToMainMenu("Items Have Been Added")

    elif userChoice == '2':
        print()
        while True:
            user_item = input("Item Name: ")
            if user_item != '':
                break
        while True:
            item_amount = input("Item Amount: ")
            if item_amount.isdigit():
                break
        addItemsToFile({user_item: int(item_amount)}, clear=False)
        returnToMainMenu("Item Has Been Added")

def viewInventory():
    clear()
    print("VIEW INVENTORY")
    print("--------------")
    print()
    invItems = getInvItems()
    print("ITEMS")
    print("-----")
    print()
    for item in invItems:
        print(f"{item}: {invItems[item]}")

    print()
    print("Available Options:")
    print()
    print("1 - Edit Item")
    print("2 - Delete Item")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            editInventoryItem()
            break
        elif userChoice == '2':
            deleteInventoryItem()
            break

def editInventoryItem():
    clear()
    print("EDIT INVENTORY ITEM")
    print("-------------------")
    print("Press (B) To Go Back")
    print()
    print("Available Options")
    print()
    print("1 - Edit Item Name")
    print("2 - Edit Item Amount")
    print()
    while True:
        userChoice = input("Choose An Option: ").lower()
        if userChoice in ['1', '2', 'b']:
            break
    if userChoice == 'b':
        main()

    invItems = getInvItems()
    if userChoice == '1':
        print()
        while True:
            itemToChange = input("Enter The Name Of The Item To Edit: ")
            if itemToChange in invItems:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            newItemName = input("Enter The New Item Name: ")
            if newItemName != '':
                break
        invItems.update({newItemName: invItems[itemToChange]})
        del invItems[itemToChange]

        addItemsToFile(invItems, clear=True)
        returnToMainMenu("Item Name Has Been Changed")

    elif userChoice == '2':
        print()
        while True:
            itemToChange = input("Enter The Name Of The Item To Edit: ")
            if itemToChange in invItems:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            newAmountName = input("Enter The New Item Amount: ")
            if newAmountName != '':
                break
        invItems.update({itemToChange: newAmountName})
        addItemsToFile(invItems, clear=True)
        returnToMainMenu("Item Amount Has Been Changed")

def deleteInventoryItem():
    print("DELETE INVENTORY ITEM")
    print("---------------------")
    print()
    invItems = getInvItems()
    while True:
        itemToDelete = input("Enter The Name Of The Item To Delete: ")
        if itemToDelete in invItems:
            break
        else:
            print("That Item Does Not Exist")
            print()

    while True:
       confirmation = input("CONFIRMATION: Are You Sure You Want To Delete This Item: ").lower()
       if confirmation in ['yes', 'no']:
           break
    if confirmation == 'yes':
        del invItems[itemToDelete]
        addItemsToFile(invItems, clear=True)
        returnToMainMenu("Item Has Been Deleted")
    else:
        main()

def addItemsToFile(userItems: dict, clear: bool):
    if clear:
        f = open('userItems.txt', 'w')
        f.close()
        with open('userItems.txt', 'a') as file:
            for item in userItems:
                file.write(f"{item}: {userItems[item]}")
                file.write('\n')
        return
    invItems = getInvItems()
    for item in userItems:
        # CHECK IF THE ITEM HAS ALREADY BEEN ADDED
        if item in invItems:
            invItems[item] += userItems[item]
    with open('userItems.txt', 'a') as file:
        for item in invItems:
            file.write(f"{item}: {invItems[item]}")
            file.write('\n')

def getInvItems():
    invItems = {}
    with open('userItems.txt', 'r') as file:
        for line in file:
            line = line.replace('\n','').split(':')
            itemName, itemAmount = line[0], line[1].strip()
            invItems.update({itemName: int(itemAmount)})

    return invItems

def returnToMainMenu(message):
    while True:
        print()
        back = input(f"{message}. Press (M) To Return To Main Menu: ").lower() if message != None else input("Press (M) To Return To Main Menu: ").lower()
        if back == 'm':
            main()
            break


main()
