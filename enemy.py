"""Definition of enemy."""
from persons import Persons
from controllers import collisionChecker, editMatrix
from random import randint


class Enemy(Persons):
    """Enemy class."""

    def __init__(self, length, breadth):
        """Make an enemy."""
        Persons.__init__(self, length, breadth)
        self.nextX = None
        self.nextY = None
        self.direction = None
        self.matrix = [['{', '*', '*', '}'], [' ', ']', '[', ' ']]

    def randomPlace(self, brdObject):
        """Place an enemy randomly."""
        flag = 1
        while flag != 0:
            a = 4 * randint(1, 7)
            b = 2 * randint(1, 30)
            if collisionChecker(brdObject, self, a, b) == 0:
                editMatrix(brdObject, self, a, b)
                self.place(a, b)
                flag = 0

    def randomMove(self, brdObject, temp):
        """Move an enemy ranomly."""
        if self.destroyed is True:
            return
        else:
            if temp == 0:
                self.moveRight(brdObject)
            elif temp == 1:
                self.moveLeft(brdObject)
            elif temp == 2:
                self.moveUp(brdObject)
            elif temp == 3:
                self.moveDown(brdObject)
