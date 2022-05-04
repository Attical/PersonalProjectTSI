from sys import displayhook
from player import Player
from cpu import Cpu

class TicTacToe():

    def __init__(self, player, cpu, display, input_adaptor):
        self.player = player
        self.cpu = cpu
        self.display = display
        self.input = input_adaptor
        
    def createDefaultBoard(self):
        board = {
            "t" : ["","",""],
            "m" : ["","",""],
            "b" : ["","",""]
        }

        return board

    def showBoard(self, board):
        for x in board:
            print(board[x][0], "|", board[x][1], "|", board[x][2]) 
        self.display.display("\n")

    def placeInPosition(self, board, role, user): #this function could probably work for both CPU and Player
        if user == "player":
            listOfPosition = self.player.getPosition()
            row = listOfPosition[0]
            value = listOfPosition[1]
        if user == "cpu":
            listOfPosition = self.cpu.getPosition(board)
            row = listOfPosition[0]
            value = listOfPosition[1]


        if row == "t":
            board["t"][int(value)-1] = role 

        if row == "m":
            board["m"][int(value)-1] = role

        if row == "b":
            board["b"][int(value)-1] = role

        return board
    
    def horizontalState(self, board): #horizontal win state
        state = False
        for x in board:
            if board[x][0] != "":
                if board[x][0] == board[x][1] == board[x][2]:
                    state = True
        return state

    def verticalState(self, board):
        state = False
        for x in range(0,3):
            if board["t"][x] != "":
                if board["t"][x] == board["m"][x] == board["b"][x]:
                    state = True
        return state

    def diagonalState(self, board):
        state = False
        if board["m"][1] != "":
            if board["t"][0] == board["m"][1] == board["b"][2] or board["t"][2] == board["m"][1] == board["b"][0]:
                state = True
        return state

    def drawState(self, board):
        state = False
        counter = 0
        for x in board:
            for y in board[x]:
                if y != "":
                    counter += 1
        if counter == 9:
            state = True

        return state

    def runGame(self, playerRole, cpuRole, board):
        game = True
        while game == True:
            board = self.placeInPosition(board, playerRole, "player")

            hor = self.horizontalState(board)
            ver = self.verticalState(board)
            dia = self.diagonalState(board)
            draw = self.drawState(board)

            if hor or ver or dia or draw:
                self.showBoard(board)
                game = False
                break
            
            board = self.placeInPosition(board, cpuRole, "cpu") 
            self.showBoard(board)
        
    
        self.display.display("Game finished")

    