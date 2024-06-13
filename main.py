#defined data
data = ["name", "age", "occ"]

data.pop(0)
data.pop(1)
data.pop(0)

#Classes for code function


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


name = nameFunction.name.upper()
age = ageFunction.age.upper()
occ = occFunction.occ.upper()

data.append([name, age, occ])
print(data)


class confFunction:
    while data:
        print("So just to confirm, your name is " + name + ". You're " + age + " years old and your occupation is " + occ)
        print("is that correct?")
        confirm = input().upper()
        match confirm:
            case "YES":
                print("Perfect, thank you!")
                print(data)
                break
            case "NO":
                print("Oh, apologies. What changes do you want made? Please enter 'Name', 'Age' or 'Job'")
                while confirm:
                    change = input()
                    match change:
                        case "Name":
                            print("Oh, what is your name?")
                            name = input()
                            while name:
                                if name.isnumeric():
                                    print("Please enter a valid name")
                                    name = input()
                                    continue
                                else:
                                    print("Apologies " + name + "! It won't happen again")
                                    data[0][0] = name
                                    print(data)
                                    print("Are there any other changes you'd like made?")
                                    break
                            continue
                        case "Age":
                            print("Oh, how old are you?")
                            age = input()
                            while age:
                                if age.isnumeric():
                                    print("Apologies " + name + "! It won't happen again")
                                    data[0][1] = age
                                    print(data)
                                    print("Are there any other changes you'd like made?")
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
                                    print("Apologies " + name + "! It won't happen again")
                                    data[0][2] = occ
                                    print(data)
                                    print("Are there any other changes you'd like made?")
                                    break
                            continue
                        case "None":
                            print("All good, no problem!")
                            print(data)
                            break
                        case default:
                            print("Please enter Name, Age or Job. If there are no changes you want made, type None")
                            continue
                break
            case default:
                print("Please enter Yes or No")
                continue




##executable
nameFunction()
ageFunction()
occFunction()
confFunction()