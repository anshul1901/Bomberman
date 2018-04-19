"""Controllers."""


def editMatrix(brdObject, item, x, y):
    """Edit the board."""
    brd = brdObject.getMatrix()
    itemMatrix = item.getMatrix()
    for i in range(0, item.length):
        for j in range(0, item.breadth):
            brd[x + i][y + j] = itemMatrix[i][j]
    brdObject.edit(brd)


def collisionChecker(brdObject, item, x, y):
    """Check for collisions."""
    brd = brdObject.getMatrix()
    oldX = item.x
    oldY = item.y

    for i in range(oldX, oldX + item.length):
        for j in range(oldY, oldY + item.breadth):
            brd[i][j] = ' '

    for i in range(x, x + item.length):
        for j in range(y, y + item.breadth):
            if brd[i][j] != ' ':
                editMatrix(brdObject, item, oldX, oldY)
                return -1

    return 0
