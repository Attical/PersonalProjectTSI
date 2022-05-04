from tictactoe import TicTacToe
from player import Player
from cpu import Cpu

class Main:
    def main():
        player = Player()
        cpu = Cpu()
        tictactoe = TicTacToe(player, cpu)
        
        #probably display and input adapter stuff here

if __name__ == '__main__':
    Main.main()
    
#IMPORTANT COMMENT, I SHOULD PROBABLY GO THROUGH ALL CODE AND COMMENT IT FOR CLEAN CODING MARKS