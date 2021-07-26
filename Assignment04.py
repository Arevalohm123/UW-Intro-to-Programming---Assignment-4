# _______________________________________________________#
# Assignment #4
# Dev: Andrei Arevalo
# Date: January 23rd, 2021
# ChangeLog:
# AArevalo, 1/23,2021, Initial Revision
# _______________________________________________________#

# Assignment Task: Create a program that asks the user for the name
#   of a household item, and then asks for its estimated value.
#   Store both pieces of data in a two-dimensional list, where each
#   item and price area a row of data, and each row is part of a
#   table of data
# _______________________________________________________#

Data = []
choice = None

while choice != "3":
    print(
        """
        Menu of Options
        1) Add data to list
        2) Display Current Data
        3) Exist and Save to File
        """
    )

    choice = input("Which option would you life to perform? [1-3]")
    print()

    if choice == "1":
        name = input("What item would you like to add?:")
        value = input("How much is this item worth in dollars?:")
        entry = (name, value)
        Data.append(entry)

    elif choice == "2":
        print("Name\t\tValue")
        print("----------------------")
        for entry in Data:
            name, value = entry
            print(name, "\t\t", "$" + value)

    elif choice == "3":
        import os
        os.remove("C:\\_PythonClass1\\Assignment04\\HouseInventory.txt")
        objFile = open("C:\\_PythonClass1\\Assignment04\\HouseInventory.txt", "a")
        for entry in Data:
            name, value = entry
            objFile.write(name + "," + value + "\n")
        objFile.close()
        print("You're file has been saved. Good-bye")

    # 