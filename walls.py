"""Walls."""


from controllers import editMatrix


class Walls(object):
    """Class walls."""

    def __init__(self, length, breadth):
        """Make the wall."""
        self.length = length
        self.breadth = breadth
        self.matrix = []

        for i in range(0, self.length):
            self.matrix.append([])
            for j in range(0, self.breadth):
                self.matrix[i].append('x')

    def makeBoundary(self, brdObject):
        """Make the boundary."""
        brd = brdObject.getMatrix()
        for j in range(0, 4):
            for i in range(0, brdObject.length):
                brd[i][j] = 'x'

        for i in range(0, 2):
            for j in range(0, brdObject.breadth):
                brd[i][j] = 'x'

        for i in range(brdObject.length - 2, brdObject.length):
            for j in range(0, brdObject.breadth):
                brd[i][j] = 'x'

        for j in range(brdObject.breadth - 4, brdObject.breadth):
            for i in range(0, brdObject.length):
                brd[i][j] = 'x'

        x = 4
        y = 8
        while x < (brdObject.length - 4):
            while y < (brdObject.breadth - 8):
                editMatrix(brdObject, self, x, y)
                y += 4 + self.breadth
            x += 2 + self.length
            y = 8

    def getMatrix(self):
        """Return the matrix."""
        return self.matrix
