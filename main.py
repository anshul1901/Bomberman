"""Starts the game."""
from board import Board
from walls import Walls
from player import Player
from enemy import Enemy
from brick import Bricks
from bomb import Bomb
from inputs import input_to
from random import randint
import os
import sys

brd = Board(34, 68)
wall = Walls(2, 4)
wall.makeBoundary(brd)
plr = Player(2, 4)
plr.insertNew(brd, 2, 4)
bmb = Bomb(2, 4)

enemy = []
for i in range(0, 5):
    enemy.append(Enemy(2, 4))
    enemy[i].randomPlace(brd)

bricks = []
for i in range(0, 20):
    bricks.append(Bricks(2, 4))
    bricks[i].randomPlace(brd)

while True:
    move = input_to()
    os.system("tput reset")
    print(brd.printMatrix())

    if move == 'q' or move == 'Q':
        sys.exit()

    elif move == 'd' or move == 'D':
        plr.moveRight(brd)

    elif move == 'a' or move == 'A':
        plr.moveLeft(brd)

    elif move == 's' or move == 'S':
        plr.moveDown(brd)

    elif move == 'w' or move == 'W':
        plr.moveUp(brd)

    elif move == 'b' or move == 'B':
        bmb.placeBomb(brd, plr.x, plr.y)

    bmb.updateBomb(brd, bricks, enemy, plr)

    for i in range(0, 5):
        temp = randint(0, 3)
        enemy[i].randomMove(brd, temp)
