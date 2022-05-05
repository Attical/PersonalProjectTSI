import sys
sys.path.append('C:\\Users\\Kyle\\OneDrive - University of Glasgow\\Desktop\\PersonalProject\\PersonalProjectTSI') #hard coded, but other ways wouldnt work
import unittest
from player import Player
from input import *
from display import *

class tests_fake(unittest.TestCase):
    def test_playerInput(self):
        input = TestInput("m2")
        display = ConsoleDisplay() #could maybe use the stub here? no clue
        player = Player(display,input)
        fakedList = player.getPosition()
        print(fakedList)

        self.assertTrue(["m", "2"], fakedList)


if __name__ == "__main__":
    unittest.main()
