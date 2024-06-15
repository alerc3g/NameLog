# Version 0.4 Changes -
# 1. Added ability to view entries in a list
# 2. Added range to the age checks
# 3. Added ability to delete only certain entries
# 4. General cleanup

# PLANNED CHANGES -
# 1. Display only certain entries or all entries
# 2. Delete only certain entries or all entries
# 3. Write to CSV



data = []

newdata = []

NewEntryCreated = True

print("Please create your profile for use!")

# Where the actual program runs
def MenuFunction():
    NewEntryCreated = False
    print("Hello, " + str(data[0][0]) + " and welcome to the program, what would you like to do?")
    print("TYPE C TO CREATE A NEW ENTRY")
    print("TYPE P TO DISPLAY YOUR CURRENT DATA")
    print("TYPE D TO DELETE AN ENTRY")
    print("TYPE N TO LEAVE THE SOFTWARE")
    menu = input()
    while menu:
        match menu:
            case "C":
                print("Please follow the instructions and create a new entry!")
                print("If you want to stop this entry, just type 'N' during the creation process")
                NewEntryCreated = True
                break
            case "D":
                if data == []:
                    print("There is no data to be deleted! Please type C to create a new data set")
                    print("Your current data set is " + str(data))
                    menu = input()
                else:
                    print("Please enter the number of the data set you want deleted!")
                    print("If you want to stop the deletion, please type 'N' to stop.")
                    remove = input()
                    while remove:
                        if remove == "N":
                            print("Successfully ended!")
                            menu = input()
                            break
                        elif remove.isalpha():
                            print("Please enter a valid number")
                            remove = input()
                            continue
                        elif remove.isnumeric():
                            x = int(remove)
                            if len(data) < x:
                                print("Please enter a valid number")
                                remove = input()
                                continue
                            else:
                                delete = int(x) - 1
                                data.pop([delete][0])
                                print("Removed!")
                                print("Your current data set is " + str(data))
                                menu = input()
                                break
                continue
            case "P":
                print("Certainly! Here are all your records!")
                if data == []:
                    print("There is no data to print! Please type C to create a new data set")
                    menu = input()
                    continue
                else:
                    for x in data:
                        print(x)
                    print("Here are all your entries!")
                    menu = input()
                    continue
            case "N":
                print("Are you sure you'd like to exist the program? Type 1 if you would, type 0 if you wouldn't")
                exitinput = input()
                match exitinput:
                    case "1":
                        print("Goodbye!")
                        quit()
                    case "0":
                        print("Okay!")
                        menu = input()
                        continue
            case default:
                print("Please type either C, D, or N")
                menu = input()
                continue

while NewEntryCreated:

    # Classes for code function

    class nameFunction:
        print("What is your name?")
        name = input()
        while name:
            if name.isnumeric():
                print("please enter a valid name")
                name = input()
                continue
            elif name == "N":
                if data == []:
                    print("We can't end it if there are no entries")
                    name = input()
                    continue
                else:
                    print("Successfully ended!")
                    MenuFunction()
            else:
                print("Hello " + name)
                break


    class ageFunction:
        print("How old are you?")
        age = input()
        while age:
            if age == "N":
                if data == []:
                    print("We can't end it if there are no entries")
                    age = input()
                    continue
                else:
                    print("Successfully ended!")
                    MenuFunction()
            elif age.isalpha():
                print("Please enter a valid age")
                age = input()
                continue
            elif age.isnumeric():
                z = int(age)
                if z < 101:
                    print("So you're " + str(z) + "?")
                    break
                else:
                    print("Please enter a value in the range of 0 - 100")
                    age = input()
                    continue


    class occFunction:
        print("What do you do for a living?")
        occ = input()
        while occ:
            if occ.isnumeric():
                print("Please input a valid occupation")
                occ = input()
                continue
            elif occ == "N":
                if data == []:
                    print("We can't end it if there are no entries")
                    occ = input()
                    continue
                else:
                    print("Successfully ended!")
                    MenuFunction()
            else:
                break


    name = nameFunction.name
    age = ageFunction.age
    occ = occFunction.occ

    newdata = [name, age, occ]

    data.append(newdata)


    class confFunction:
        while data:
            print("Just to confirm this is your data set? " + str(newdata))
            print("is that correct? Please enter Yes or No")
            confirm = input().upper()
            match confirm:
                case "YES":
                    print("Perfect, thank you!")
                    MenuFunction()
                    break
                case "NO":
                    print("Oh, What changes do you made? Please enter 'Name', 'Age' or 'Job'")
                    while confirm:
                        change = input()
                        match change:
                            case "Name":
                                print("Oh, What is your name?")
                                name = input()
                                while name:
                                    if name.isnumeric():
                                        print("Please enter a valid name")
                                        name = input()
                                        continue
                                    else:
                                        print("Thank you " + name + "! Changes have been applied")
                                        newdata[0] = name
                                        print(newdata)
                                        print("Thank you, if you want any other changes made please type either 'Name', 'Age' or 'Job'")
                                        break
                                continue
                            case "Age":
                                print("Oh, how old are you?")
                                age = input()
                                while age:
                                    if age.isnumeric():
                                        z = int(age)
                                        if z < 101:
                                            print("Thank you " + name + "! Changes have been applied")
                                            newdata[1] = age
                                            print(newdata)
                                            print("Thank you, if you want any other changes made please type either 'Name', 'Age' or 'Job'")
                                        else:
                                            print("Please enter a value in the range of 0 - 100")
                                            age = input()
                                            continue
                                        break
                                    else:
                                        print("Please enter a valid age")
                                        age = input()
                                        continue
                                continue
                            case "Job":
                                print("Oh, what is your Job?")
                                occ = input()
                                while occ:
                                    if occ.isnumeric():
                                        print("Please enter a valid job")
                                        occ = input()
                                        continue
                                    else:
                                        print("Thank you " + name + "! Changes have been applied")
                                        newdata[2] = occ
                                        print(newdata)
                                        print("Thank you, if you want any other changes made please type either 'Name', 'Age' or 'Job'")
                                        break
                                continue
                            case "None":
                                print("All good, no problem!")
                                print(newdata)
                                MenuFunction()
                                break
                            case default:
                                print("Please enter Name, Age or Job. If there are no changes you want made, type None")
                                continue
                    break
                case default:
                    print("Please enter Yes or No")
                    continue
