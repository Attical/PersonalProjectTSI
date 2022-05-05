import random

class Cpu:
    def getRole(self, playerRole):
        if playerRole == "x":
            cpuRole = "o"
        if playerRole == "o":
            cpuRole = "x"

        return cpuRole

    def isSpaceAvailable(self, board, row, value):
        if board[row][value-1] == "":
            return True
        if board[row][value-1] != "":
            return False
            

    def getPosition(self, board):
        listOfPosition = []

        available = False
        while available == False:
            row = random.randint(1,3) 
            value = random.randint(1,3)

            if row == 1:
                row = "t"
            if row == 2:
                row = "m"
            if row == 3:
                row = "b"

            available = self.isSpaceAvailable(board, row, value)

        listOfPosition.append(row)
        listOfPosition.append(value)

        return listOfPosition #[t,2] for example
