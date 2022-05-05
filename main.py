from tictactoe import TicTacToe
from player import Player
from cpu import Cpu
from display import *
from input import *

class Main:
    def main():
        display = ConsoleDisplay()
        input_adaptor = ConsoleInput()
        player = Player(display, input_adaptor)
        cpu = Cpu()
        tictactoe = TicTacToe(player, cpu, display, input_adaptor)

        playerRole = player.assignRole()
        board = tictactoe.createDefaultBoard()
        display.display("Welcome to TicTacToe!") 
        tictactoe.showBoard(board)
        cpuRole = cpu.getRole(playerRole)

        tictactoe.runGame(playerRole, cpuRole, board)


if __name__ == '__main__':
    Main.main()
