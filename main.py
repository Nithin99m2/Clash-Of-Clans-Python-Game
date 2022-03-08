from Screen import Board
from os import system
from King import king
import time

board = Board()

# In order to follow coordinate system, (x,y) needs to be written in [y][x] format, where y grows downwards.


while(1):
    g=board.king.move(board)
    s=board.king.attack(board)
    if(g=='q'):
        system('clear')
        break
    else:
        
        board.render()

    continue

    
