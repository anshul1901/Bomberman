"""Persons."""

from controllers import editMatrix, collisionChecker


class Persons(object):
    """Class person."""

    def __init__(self, length, breadth):
        """Make the person."""
        self.length = length
        self.breadth = breadth
        self.matrix = []
        self.x = 2
        self.y = 4
        self.destroyed = False

    def insertNew(self, brdObject, x, y):
        """Insert the person."""
        if collisionChecker(brdObject, self, x, y) == 0:
            editMatrix(brdObject, self, x, y)
            self.place(x, y)
            return 0
        return -1

    def place(self, x, y):
        """Place the person."""
        self.x = x
        self.y = y

    def getMatrix(self):
        """Return the matrix."""
        return self.matrix

    def moveRight(self, brdObject):
        """Move the person right."""
        if collisionChecker(brdObject, self, self.x, self.y + 1) == 0:
            editMatrix(brdObject, self, self.x, self.y + 1)
            self.place(self.x, self.y + 1)
        else:
            return 1

    def moveLeft(self, brdObject):
        """Move the person left."""
        if collisionChecker(brdObject, self, self.x, self.y - 1) == 0:
            editMatrix(brdObject, self, self.x, self.y - 1)
            self.place(self.x, self.y - 1)
        else:
            return 1

    def moveUp(self, brdObject):
        """Move the person up."""
        if collisionChecker(brdObject, self, self.x - 1, self.y) == 0:
            editMatrix(brdObject, self, self.x - 1, self.y)
            self.place(self.x - 1, self.y)
        else:
            return 1

    def moveDown(self, brdObject):
        """Move the person down."""
        if collisionChecker(brdObject, self, self.x + 1, self.y) == 0:
            editMatrix(brdObject, self, self.x + 1, self.y)
            self.place(self.x + 1, self.y)
        else:
            return 1

    def destroy(self, brdObject):
        """Destroy the person."""
        if self.destroyed is False:
            self.destroyed = True
            for i in range(0, self.length):
                for j in range(0, self.breadth):
                    self.matrix[i][j] = ' '
            editMatrix(brdObject, self, self.x, self.y)
            brdObject.score += 100
