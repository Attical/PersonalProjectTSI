import sys
sys.path.append('C:\\Users\\Kyle\\OneDrive - University of Glasgow\\Desktop\\PersonalProject\\PersonalProjectTSI') #hard coded, but other ways wouldnt work
import unittest
from player import Player
from input import *
from display import *
from cpu import Cpu
from tictactoe import TicTacToe

class tests_unittests(unittest.TestCase):

    def test_placeInPositionPlayer(self):
        display = ConsoleDisplay()
        input_adaptor = TestInput("t1")
        player = Player(display, input_adaptor)
        cpu = Cpu()
        test_instance = TicTacToe(player,cpu,display,input_adaptor)

        board = {
            "t" : ["","",""],
            "m" : ["","",""],
            "b" : ["","",""]
        }


        board = test_instance.placeInPosition(board,"x","player")

        self.assertEqual(board, {
            "t" : ["x","",""],
            "m" : ["","",""],
            "b" : ["","",""]
        })


if __name__ == "__main__":
    unittest.main()