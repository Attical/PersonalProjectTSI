class DisplayInterface:
    def display(self, string):
        pass


class ConsoleDisplay(DisplayInterface):
    def display(self, string):
        print(string)
        pass


class TestDisplay(DisplayInterface):

    def __init__(self):
        self.capture = "fish"

    def display(self, string):
        self.capture = str(string)
        pass

    def report(self):
        return self.capture
