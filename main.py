data = ["name", "age", "occ"]

data.pop(0)
data.pop(1)
data.pop(0)


class nameFunction:
    print("What is your name?")
    name = input()
    print("Hello " + name)


class ageFunction:
    print("How old are you?")
    age = input()
    print("So you're " + age + "?")


class occFunction:
    print("What do you do for a living?")
    occ = input()


nameFunction()
ageFunction()
occFunction()

name = nameFunction.name
age = ageFunction.age
occ = occFunction.occ

data.append([name, age, occ])
print(data)

print("So just to confirm, your name is " + name + ". You're " + age + " years old and your occupation is " + occ)
print("is that correct?")

confirm = input()
if confirm == "Yes":
    print("Perfect, thank you!")
    print(data)
elif confirm == "No":
    print("Oh, apologies. What changes do you want made?")
    while confirm:
        change = input()
        match change:
            case "Name":
                print("Oh, what is your name?")
                name = input()
                print("Apologies " + name + "! It won't happen again")
                data[0][0] = name
                print(data)
                print("Are there any other changes you'd like made?")
                continue
            case "Age":
                print("Oh, how old are you?")
                age = input()
                print("Apologies " + name + "! It won't happen again")
                data[0][1] = age
                print(data)
                print("Are there any other changes you'd like made?")
                continue
            case "Job":
                print("Oh, what is your Job?")
                occ = input()
                print("Apologies " + name + "! It won't happen again")
                data[0][2] = occ
                print(data)
                print("Are there any other changes you'd like made?")
                continue
            case "None":
                print("All good, no problem!")
                print(data)
                break
