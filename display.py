class DisplayInterface:
    def display(self, string):
        pass


class ConsoleDisplay(DisplayInterface):
    def display(self, string):
        print(string)
        pass
