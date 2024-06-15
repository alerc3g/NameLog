def MenuFunction():
    NewEntryCreated = False
    print("Hello, " + str(data[0][0]) + " and welcome to the program, what would you like to do?")
    print("TYPE C TO CREATE A NEW ENTRY")
    print("TYPE D TO DELETE YOUR PREVIOUS ENTRY")
    print("TYPE N TO LEAVE THE SOFTWARE")
    print("Your current data set is " + str(data))
    menu = input()
    while menu:
        match menu:
            case "C":
                print("Please follow the instructions and create a new entry!")
                NewEntryCreated = True
                break
            case "D":
                if data == []:
                    print("You can't delete anything!")
                    print("Your current data set is " + str(data))
                    menu = input()
                else:
                    print("Deleted!")
                    data.pop([0][0])
                    print("Your current data set is " + str(data))
                    menu = input()
                continue
            case "N":
                print("Very well, goodbye!")
                quit()
            case default:
                print("Please type either C, D, or N")
                menu = input()
                continue

#defined data

data = []

NewEntryCreated = True

print("Please create your profile for use!")

while NewEntryCreated:
    newdata = []


    # Classes for code function

    class nameFunction:
        print("What is your name?")
        name = input()
        while name:
            if name.isnumeric():
                print("please enter a valid name")
                name = input()
                continue
            else:
                print("Hello " + name)
                break


    class ageFunction:
        print("How old are you?")
        age = input()
        while age:
            if age.isnumeric():
                print("So you're " + age + "?")
                break
            else:
                print("Please enter a valid age")
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
            else:
                break


    name = nameFunction.name
    age = ageFunction.age
    occ = occFunction.occ

    newdata = [name, age, occ]

    data.append(newdata)
    print(newdata)


    class confFunction:
        while data:
            print(
                "So just to confirm, your name is " + name + ". You're " + age + " years old and your occupation is " + occ)
            print("is that correct?")
            confirm = input().upper()
            match confirm:
                case "YES":
                    print("Perfect, thank you!")
                    print(newdata)
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
                                        print("Thank you " + name + "! Changes have been applied")
                                        newdata[1] = age
                                        print(newdata)
                                        print("Thank you, if you want any other changes made please type either 'Name', 'Age' or 'Job'")
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
