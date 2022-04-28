import random

class Cpu:
    def getRole(playerRole):
        if playerRole == "x":
            cpuRole = "o"
        if playerRole == "o":
            cpuRole = "x"

        return cpuRole

    def isSpaceAvailable(board, row, value):
        if board[row][value-1] == "":
            return True
        if board[row][value-1] != "":
            return False
            

    def getPosition(board):
        listOfPosition = []

        available = False
        while available == False:
            row = random.randint(1,3) #1= t1, 2= t2 etc.
            value = random.randint(1,3)

            if row == 1:
                row = "t"
            if row == 2:
                row = "m"
            if row == 3:
                row = "b"

            available = Cpu.isSpaceAvailable(board, row, value)

        listOfPosition.append(row)
        listOfPosition.append(value)

        return listOfPosition #[t,2] for example


    #can maybe use inheritance from player class? to avoid more rewriting + big brain
    #can do multiple tests for if the cpu logic works as intended