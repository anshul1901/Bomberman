from persons import Persons


class Player(Persons):
    def __init__(self, length, breadth):
        Persons.__init__(self, length, breadth)
        self.matrix = [['[', '^', '^', ']'], [' ', ']', '[', ' ']]
