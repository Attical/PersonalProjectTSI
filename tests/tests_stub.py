from display import *
import unittest

class DisplayStub(DisplayInterface):
    def __init__(self):
        self.loc = "m3"

    def display(self, string):
        self.loc = str(string)
        pass

    def report(self):
        return self.loc

