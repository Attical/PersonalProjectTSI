import random

class Player:
    def assignRole():
        playerXorO = random.randint(1,2)

        if playerXorO == 1:
            playerXorO = "o"
        else:
            playerXorO = "x"

        print("You have been assigned %s" % playerXorO)

        return playerXorO

    def getPosition():
        role = Player.assignRole()
        position = input("Choose where you would like to place, type a row (t/m/b) with a number. For example m3")

        listOfPosition = []
        for x in position:
            listOfPosition.append(x)

        return listOfPosition

    def placeInPosition():
        listOfPosition = Player.getPosition()
        row = listOfPosition[0]
        value = listOfPosition[1]

        print(row, value)

#ideas for testing:
# assignROles() check if truly random


#what can a player do:
#IDEA FOR REFACTORING:
#make class initially have it so that it has 2 functions, one called place X and one called placeO
#then REFACTOR it to make it just one function called place

#func place x/o

