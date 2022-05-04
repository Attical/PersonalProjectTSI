class InputInterface:
    def get_string(self, message):
        pass


class ConsoleInput(InputInterface):
    def get_string(self, message):
        return input(message)


class TestInput(InputInterface):
    def get_string(self, message):
        return(self.return_string)
    
    def __init__(self,return_string):
        self.return_string = return_string
