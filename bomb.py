"""Definition of Bomb."""
from controllers import editMatrix
import time


class Bomb(object):
    """Bomb class."""

    def __init__(self, length, breadth):
        """Make the bomb."""
        self.length = length
        self.breadth = breadth
        self.createdAt = None
        self.x = None
        self.y = None
        self.count = 0
        self.matrix = []

        for i in range(0, self.length):
            self.matrix.append([])
            for j in range(0, self.breadth):
                self.matrix[i].append('3')

    def placeBomb(self, brdObject, x, y):
        """Place the bomb randomly."""
        if self.count == 0:
            self.createdAt = time.time()
            self.x = x
            self.y = y
            self.count = 1
            editMatrix(brdObject, self, x, y)

    def updateBomb(self, brdObject, bricks, enemy, plr):
        """Update the bomb."""
        if self.createdAt is not None:
            stamp = time.time() - self.createdAt
            if stamp <= 1 and stamp > 0:
                editMatrix(brdObject, self, self.x, self.y)
            elif stamp <= 2 and stamp > 1:
                for i in range(self.x, self.x + self.length):
                    for j in range(self.y, + self.y + self.breadth):
                        brdObject.matrix[i][j] = '2'
            elif stamp <= 3 and stamp > 2:
                for i in range(self.x, self.x + self.length):
                    for j in range(self.y, + self.y + self.breadth):
                        brdObject.matrix[i][j] = '1'
            else:
                for i in range(self.x, self.x + self.length):
                    for j in range(self.y, + self.y + self.breadth):
                        brdObject.matrix[i][j] = ' '
                self.explodeBomb(brdObject, bricks, enemy, plr)
                self.createdAt = None
                self.count = 0

    def explodeBomb(self, brdObject, bricks, enemy, plr):
        """Explode the bomb."""
        for i in range(self.x - 2, self.x):
            for j in range(self.y, self.y + 4):
                for k in range(0, 20):
                    if i >= bricks[k].x and i < bricks[k].x + 2 and \
                       j >= bricks[k].y and j < bricks[k].y + 4:
                        bricks[k].destroy(brdObject)
                for l in range(0, 5):
                    if i >= enemy[l].x and i < enemy[l].x + 2 and \
                       j >= enemy[l].y and j < enemy[l].y + 4:
                        enemy[l].destroy(brdObject)
                if i >= plr.x and i < plr.x + 2 and \
                   j >= plr.y and j < plr.y + 4:
                    plr.destroy(brdObject)
        for i in range(self.x, self.x + 2):
            for j in range(self.y - 4, self.y):
                for k in range(0, 20):
                    if i >= bricks[k].x and i < bricks[k].x + 2 and \
                       j >= bricks[k].y and j < bricks[k].y + 4:
                        bricks[k].destroy(brdObject)
                for l in range(0, 5):
                    if i >= enemy[l].x and i < enemy[l].x + 2 and \
                       j >= enemy[l].y and j < enemy[l].y + 4:
                        enemy[l].destroy(brdObject)
                if i >= plr.x and i < plr.x + 2 and \
                   j >= plr.y and j < plr.y + 4:
                    plr.destroy(brdObject)
        for i in range(self.x, self.x + 2):
            for j in range(self.y + 4, self.y + 8):
                for k in range(0, 20):
                    if i >= bricks[k].x and i < bricks[k].x + 2 and \
                       j >= bricks[k].y and j < bricks[k].y + 4:
                        bricks[k].destroy(brdObject)
                for l in range(0, 5):
                    if i >= enemy[l].x and i < enemy[l].x + 2 and \
                       j >= enemy[l].y and j < enemy[l].y + 4:
                        enemy[l].destroy(brdObject)
                if i >= plr.x and i < plr.x + 2 and \
                   j >= plr.y and j < plr.y + 4:
                    plr.destroy(brdObject)
        for i in range(self.x + 2, self.x + 4):
            for j in range(self.y, self.y + 4):
                for k in range(0, 20):
                    if i >= bricks[k].x and i < bricks[k].x + 2 and \
                       j >= bricks[k].y and j < bricks[k].y + 4:
                        bricks[k].destroy(brdObject)
                for l in range(0, 5):
                    if i >= enemy[l].x and i < enemy[l].x + 2 and \
                       j >= enemy[l].y and j < enemy[l].y + 4:
                        enemy[l].destroy(brdObject)
                if i >= plr.x and i < plr.x + 2 and \
                   j >= plr.y and j < plr.y + 4:
                    plr.destroy(brdObject)

    def getMatrix(self):
        """Return bomb."""
        return self.matrix
