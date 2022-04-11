
import os
def readln():

    if os.path.isfile("data1.txt"):
        with open("data1.txt", "r") as file:
            return file.readline()
    else:
        return None

class animals:
    def __init__(self,animal): #splits animal list
        self.animalStuff = animal.split(" ")


    def isMatch (self, ourAnimalProperties,numQuestions): #checks for a match
        match = True
        for i in range(0,numQuestions - 1):
            if ourAnimalProperties[i] != self.animalStuff[i+1]:
                match = False
                break
        return match, self.animalStuff[0]

readln()
qa = open("data.txt", 'r')
ouranimal = []
zoo = []

animalnum = int(qa.readline().strip("\nw"))
qnum = int(qa.readline().strip("\n"))
print("think of an animal (within the list smartie)")
for i in range(0,qnum):
    ouranimal.append(input(qa.readline()))
print(ouranimal)

# for i in range(0,qnum):
#
#     zoo.append(qa.readline())



for i in range(0,animalnum):
    zoo.append(animals(qa.readline().strip("\n")))
    match, animal = zoo[i].isMatch(ouranimal,qnum)


if match:
    print("Is this animal A " + animal)
else:
    while match == False:
        qmod = open("data.txt", 'a')
        newname = input("what is this animal ")
        nanimal = " ".join(ouranimal)
        qmod.write("\n" + newname + " " + nanimal)
        break
print("New animal set " + newname)