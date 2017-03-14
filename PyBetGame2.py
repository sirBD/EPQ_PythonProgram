"""Game Design = Code a game that allows simple bets to be made on a grid.
Player will get a balance at the start of each round, and scores will be stored in a file.
Game chooses a square on the grid. Player can choose grid size(4x4,6x6,8x8). Higher the score potential for the
larger grids. Seen as difficulties. Once random square is chosen, player will choose their square and both choices
will be revealed. If the player chooses the same square as the game, they get their bet multiplied by the difficulty
(grid size determines this). Potential - able to choose multiple different squares and bet different amounts.
"""

import random
import collections
import time

start_balance = (100.00)
user_options = (1,2,3)
gridoptions = ['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14','x15','x16','x17','x18','x19','x20','x21','x22','x23','x24','x25','x26']

print('Welcome to the EPQ Betting game in Python.')
time.sleep(2)
print('Use your credits to bet on on these grid squares.')
time.sleep(2)
print('If you selected the same square as the game, your betted amount will be multiplied. The bigger the grid, the bigger the multiplier.')
time.sleep(3)
print('Your starting credit balance is: ',start_balance)

def gridgenerate():
    grid1position = []
    grid2position = []
    grid3position = []
    usrinput = 0
    cellselect = 0
    
    while not usrinput in (user_options):
        print("Enter the grid difficulty [1,2,3]:")
        try:
            usrinput = int(input( ))
        except ValueError:
            usrinput not in (user_options)

    def grid1(grid1position):
        global cells
        cells = gridoptions[:9]
        grid = [cells[i:i + 3] for i in range(0, len(cells), 3)]
        for x,y,z in grid:
            print(x,y,z)

    if usrinput == 1:
        print("Selected difficulty level 1.")
        global cellselect
        cellselect = 1
        grid1(grid1position)

    def grid2(grid2position):
        global cells
        cells = gridoptions[:16]
        grid = [cells[i:i + 4] for i in range(0, len(cells), 4)]
        for w,x,y,z in grid:
            print(w,x,y,z)

    if usrinput == 2:
        print("Selected difficulty level 2.")
        global cellselect
        cellselect = 2
        grid2(grid2position)

    def grid3(grid3position):
        global cells
        cells = gridoptions[:25]
        grid = [cells[i:i + 5] for i in range(0, len(cells), 5)]
        for v,w,x,y,z in grid:
            print(v,w,x,y,z)

    if usrinput == 3:
        print("Selected difficulty level 3.")
        global cellselect
        cellselect = 3
        grid3(grid3position)

gridgenerate()

i = 0
while not i in ('yes','no'):
        print("Here is the grid, do you want to change the size?")
        try:
            i = str(input( ))
        except ValueError:
            i not in ('yes','no')
        if i == 'yes':
            gridgenerate()
        else:
            print("Game starting, good luck.")

time.sleep(2)
#Rule - User selects square on grid.
def UserSelect():
    cellselect1 = 0
    cellselect2 = 0
    cellselect3 = 0
    if cellselect == 1:
        while not cellselect1 in (cells):
            print("Select the cell you want to bet on.")
            try:
                cellselect1 = str(input( ))
            except ValueError:
                cellselect1 not in (cells)
            print("You selected cell:", cellselect1)
            time.sleep(1)
            print("Updated grid:")
            # FIX HERE for n, i in enumerate(cells):
            if i == cellselect1:
                cells[n]=("o")
                print(cells)
                
    if cellselect == 2:
        while not cellselect2 in (cells):
            print("Select the cell you want to bet on.")
            try:
                cellselect2 = str(input( ))
            except ValueError:
                cellselect2 not in (cells)
            print("You selected cell:", cellselect2)

    if cellselect == 3:
        while not cellselect3 in (cells):
            print("Select the cell you want to bet on.")
            try:
                cellselect3 = str(input( ))
            except ValueError:
                cellselect3 not in (cells)
            print("You selected cell:", cellselect3)
UserSelect()
    
