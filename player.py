import random

class Player():
    def __init__(self, display, input_adaptor):
        self.display = display
        self.input = input_adaptor

    def assignRole(self):
        playerXorO = random.randint(1,2)

        if playerXorO == 1:
            playerXorO = "o"
        else:
            playerXorO = "x"

        self.display.display("You have been assigned %s" % playerXorO)

        return playerXorO

    def getPosition(self):
        position = self.input.get_string("Choose where you would like to place, type a row (t/m/b) with a number: ")

        listOfPosition = []
        for x in position:
            listOfPosition.append(x)

        return listOfPosition

    
#ideas for testing:
# assignROles() check if truly random


#what can a player do:
#IDEA FOR REFACTORING:
#make class initially have it so that it has 2 functions, one called place X and one called placeO
#then REFACTOR it to make it just one function called place

#func place x/o

