import sys
sys.path.append('C:\\Users\\Kyle\\OneDrive - University of Glasgow\\Desktop\\PersonalProject\\PersonalProjectTSI') #hard coded, but other ways wouldnt work

import unittest
from unittest.mock import MagicMock
from tictactoe import TicTacToe
from player import Player
from cpu import Cpu
from display import *
from input import *

class test_mock(unittest.TestCase):
    def test_diaState(self):
        display = ConsoleDisplay()
        input_adaptor = ConsoleInput()
        player = Player(display, input_adaptor)
        cpu = Cpu()
        mock_test = TicTacToe(player,cpu,display,input_adaptor) 

        mock_test.createDefaultBoard = MagicMock(return_value={
                "t" : ["X","O","O"],
                "m" : ["","X",""],
                "b" : ["O","X","X"]
            }
        )
        
        board = mock_test.createDefaultBoard()

        self.assertTrue(mock_test.diagonalState(board))
    
    def test_horState(self):
        display = ConsoleDisplay()
        input_adaptor = ConsoleInput()
        player = Player(display, input_adaptor)
        cpu = Cpu()
        mock_test = TicTacToe(player,cpu,display,input_adaptor) 

        mock_test.createDefaultBoard = MagicMock(return_value={
                "t" : ["O","O","O"],
                "m" : ["","X",""],
                "b" : ["O","X","X"]
            }
        )
        
        board = mock_test.createDefaultBoard()

        self.assertTrue(mock_test.horizontalState(board))
    
    def test_verState(self):
        display = ConsoleDisplay()
        input_adaptor = ConsoleInput()
        player = Player(display, input_adaptor)
        cpu = Cpu()
        mock_test = TicTacToe(player,cpu,display,input_adaptor) 

        mock_test.createDefaultBoard = MagicMock(return_value={
                "t" : ["O","X","O"],
                "m" : ["","X",""],
                "b" : ["O","X","X"]
            }
        )
        
        board = mock_test.createDefaultBoard()

        self.assertTrue(mock_test.verticalState(board))

    def test_drawState(self):
        display = ConsoleDisplay()
        input_adaptor = ConsoleInput()
        player = Player(display, input_adaptor)
        cpu = Cpu()
        mock_test = TicTacToe(player,cpu,display,input_adaptor) 

        mock_test.createDefaultBoard = MagicMock(return_value={
                "t" : ["O","X","O"],
                "m" : ["X","O","O"],
                "b" : ["O","X","X"]
            }
        )
        
        board = mock_test.createDefaultBoard()

        self.assertTrue(mock_test.drawState(board))
    
    def test_getRole(self): #uses side effect to ensure that CPU can get its role properly
        display = ConsoleDisplay()
        input_adaptor = ConsoleInput()
        player = Player(display, input_adaptor)
        cpu = Cpu()
        mock_test = TicTacToe(player,cpu,display,input_adaptor) 

        player.assignRole = MagicMock(side_effect = ["o", "x"])

        a = cpu.getRole(player.assignRole())
        b = cpu.getRole(player.assignRole())

        self.assertNotEqual(a ,b)

if __name__ == "__main__":
    unittest.main()

#gotta implement using side_effect