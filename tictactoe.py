from player import Player
from cpu import Cpu

class TicTacToe:
    game = True

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
    
    def checkGameState(board):
        #if any three of x/o are matching, state = true (have to figure out who the winner is)
        state = True
        #horizontal win state
        for x in board:
            if board[x][0] != "":
                if board[x][0] == board[x][1] == board[x][2]:
                    state = False

        #vertical win state
        for x in range(0,2):
            if board["t"][x] != "":
                if board["t"][x] == board["m"][x] == board["b"][x]:
                    state = False

        #diagonal win state
        if board["m"][1] != "":
            if board["t"][0] == board["m"][1] == board["b"][2] or board["t"][2] == board["m"][1] == board["b"][0]:
                state = False
        
        #draw state
        counter = 0
        for x in board:
            for y in board[x]:
                if y != "":
                    counter += 1
        if counter == 9:
            state = False

        #state = true if game isnt over
        #state = false if game is over
        return state

    while game == True:
        board = placeInPosition(board, playerRole, "player")

        game = checkGameState(board)
        if game == False:
            showBoard(board)
            break
        
        board = placeInPosition(board, cpuRole, "cpu") 
        showBoard(board)
        
    
    print("Game finished")


    