from player import Player
from cpu import Cpu

class TicTacToe:
    def __init__(self, player, cpu):
        self.player = player
        self.cpu = cpu #ngl this isnt nescasary since it is never used?
        
    def createDefaultBoard():
        board = {
            "t" : ["","",""],
            "m" : ["","",""],
            "b" : ["","",""]
        }

        return board

    def showBoard(board):
        for x in board:
            print(board[x][0], "|", board[x][1], "|", board[x][2]) 
        print("\n")

    board = createDefaultBoard()
    print("Welcome to TicTacToe!")
    showBoard(board)
    playerRole = Player.assignRole()
    cpuRole = Cpu.getRole(playerRole)

    def placeInPosition(board, role, user): #this function could probably work for both CPU and Player
        if user == "player":
            listOfPosition = Player.getPosition()
            row = listOfPosition[0]
            value = listOfPosition[1]
        if user == "cpu":
            listOfPosition = Cpu.getPosition(board)
            row = listOfPosition[0]
            value = listOfPosition[1]


        if row == "t":
            board["t"][int(value)-1] = role 

        if row == "m":
            board["m"][int(value)-1] = role

        if row == "b":
            board["b"][int(value)-1] = role

        return board

    board = placeInPosition(board, playerRole, "player") #test for player
    showBoard(board)

    board = placeInPosition(board,cpuRole, "cpu") #test for cpu
    showBoard(board)

    #place = input("select where you wanna place X")

    #functions:
    #showdefaultboard
    #updateboard (on play from player/cpu class)

    #ideas for testing:
    
#until game finished:
    #placeInPosition