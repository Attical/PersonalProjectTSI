class TicTacToe:
    def __init__(self, player, cpu):
        self.player = player
        self.cpu = cpu
        
    def createDefaultBoard():
        board = {
            "row1" : ["","",""],
            "row2" : ["","",""],
            "row3" : ["","",""]
        }

        return board

    def showBoard(board):
        for x in range(1,3):
            print(board["row%s" % x][0], "|", board["row%s" % x][1], "|", board["row%s" % x][2]) 
        
    board = createDefaultBoard()
    print("Welcome to TicTacToe!")
    showBoard(board)

    #place = input("select where you wanna place X")

    #functions:
    #showdefaultboard
    #updateboard (on play from player/cpu class)
    