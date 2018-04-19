"""Generate the board."""


class Board(object):
    """Class board."""

    def __init__(self, length, breadth):
        """Make the board."""
        self.length = length
        self.breadth = breadth
        self.matrix = []
        self.score = 0

        for i in range(0, self.length):
            self.matrix.append([])
            for j in range(0, self.breadth):
                self.matrix[i].append(' ')

    def getMatrix(self):
        """Return the matrix."""
        return self.matrix

    def printMatrix(self):
        """Return the string matrix."""
        temp = ''
        for i in range(0, self.length):
            for j in range(0, self.breadth):
                temp += self.matrix[i][j]
            temp += '\n'
        temp += 'Score = ' + str(self.score)
        return temp

    def edit(self, editedMatrix):
        """Edit the matrix."""
        self.matrix = editedMatrix
