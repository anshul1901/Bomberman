"""Definition of brick."""

from controllers import editMatrix, collisionChecker
from random import randint


class Bricks():
    """Class brick."""

    def __init__(self, length, breadth):
        """Make the brick."""
        self.length = length
        self.breadth = breadth
        self.matrix = []
        self.x = 2
        self.y = 4
        self.destroyed = False

        for i in range(0, self.length):
            self.matrix.append([])
            for j in range(0, self.breadth):
                self.matrix[i].append('/')

    def randomPlace(self, brdObject):
        """Place the brick randomly."""
        flag = 1
        while flag != 0:
            a = 2 * randint(1, 15)
            b = 4 * randint(1, 15)
            if collisionChecker(brdObject, self, a, b) == 0:
                editMatrix(brdObject, self, a, b)
                self.x = a
                self.y = b
                flag = 0

    def destroy(self, brdObject):
        """Destroy the brick."""
        if self.destroyed is False:
            self.destroyed = True
            for i in range(0, self.length):
                for j in range(0, self.breadth):
                    self.matrix[i][j] = ' '
            editMatrix(brdObject, self, self.x, self.y)
            brdObject.score += 20

    def getMatrix(self):
        """.Return the matrix."""
        return self.matrix
