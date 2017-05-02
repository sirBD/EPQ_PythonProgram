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
import sys
from random import randint

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
    global cellselect
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
def BetGame():
    global multiplier
    global currentbalance
    cellselect1 = 0
    cellselect2 = 0
    cellselect3 = 0
    if cellselect == 1:
        multiplier = 2
        while not cellselect1 in (cells):
            print("Select the cell you want to bet on.")
            try:
                cellselect1 = str(input( ))
            except ValueError:
                cellselect1 not in (cells)
            print("You selected cell:", cellselect1)
            time.sleep(1)
        print("Updated grid:")
        for n, i in enumerate(cells):
            if i == cellselect1:
                cells[n]=("o")
                grid = [cells[i:i + 3] for i in range(0, len(cells), 3)]
                for x,y,z in grid:
                    print(x,y,z)
        #User selects amount of credits to bet with.
        money_input = 0
        while not money_input in range (1, 101): #does not accept float values - will limit accuracy of balances.
            print("Enter the amount you wish to bet with:")
            try:
                money_input = int(input( ))
            except ValueError:
                money_input not in range (1, 101)
        print("You are betting",money_input,"credits on cell:",cellselect1)
        def update():
            global start_balance
            start_balance = (start_balance - money_input)
            return start_balance
        update()
        currentbalance = (start_balance)
        print("Current balance =",(currentbalance))

        #Game selects a cell. Multiplier takes effect. Money rewarded/discarded.
        print("The multiplier value is:",multiplier)
        gamerandomiser = randint(1,9)
        print ("The game selected cell:")
        gamecellselect = gridoptions[gamerandomiser]
        for n, i in enumerate(cells):
            if i == gamecellselect:
                cells[n]=("$")
                grid = [cells[i:i + 3] for i in range(0, len(cells), 3)]
                for x,y,z in grid:
                    print(x,y,z)
                
        print("Cell:",gamecellselect,"!")
        if gamecellselect == cellselect1:
            print("Congratulations, you guessed correctly.")
            print("You betted:",money_input)
            reward = (money_input * multiplier)
            print("You are rewarded with:",reward,"!")
            def update2():
                global start_balance
                start_balance = (start_balance + reward)
                return start_balance
            update()
            print("Updated balance:", (start_balance))
        else:
            currentbalance = (start_balance)
            print("Unlucky! Your current balance is now:", (currentbalance))
   
                
    if cellselect == 2:
        multiplier = 3
        while not cellselect2 in (cells):
            print("Select the cell you want to bet on.")
            try:
                cellselect2 = str(input( ))
            except ValueError:
                cellselect2 not in (cells)
            print("You selected cell:", cellselect2)
            time.sleep(1)
        print("Updated grid:")
        for n, i in enumerate(cells):
            if i == cellselect2:
                cells[n]=("o")
                grid = [cells[i:i + 4] for i in range(0, len(cells), 4)]
                for w,x,y,z in grid:
                    print(w,x,y,z)
        #User selects amount of credits to bet with.
        money_input = 0
        while not money_input in range (1, 101): #does not accept float values - will limit accuracy of balances.
            print("Enter the amount you wish to bet with:")
            try:
                money_input = int(input( ))
            except ValueError:
                money_input not in range (1, 101)
        print("You are betting",money_input,"credits on cell:",cellselect2)
        def update():
            global start_balance
            start_balance = (start_balance - money_input)
            return start_balance
        update()
        currentbalance = (start_balance)
        print("Current balance =",(currentbalance))


        #Game selects a cell. Multiplier takes effect. Money rewarded/discarded.
        print("The multiplier value is:",multiplier)
        gamerandomiser = randint(1,16)
        print ("The game selected cell:")
        gamecellselect = gridoptions[gamerandomiser]
        for n, i in enumerate(cells):
            if i == gamecellselect:
                cells[n]=("$")
                grid = [cells[i:i + 4] for i in range(0, len(cells), 4)]
                for w,x,y,z in grid:
                    print(w,x,y,z)
                
        print("Cell:",gamecellselect,"!")
        if gamecellselect == cellselect1:
            print("Congratulations, you guessed correctly.")
            print("You betted:",money_input)
            reward = (money_input * multiplier)
            print("You are rewarded with:",reward,"!")
            def update2():
                global start_balance
                start_balance = (start_balance + reward)
                return start_balance
            update()
            print("Updated balance:", (start_balance))
        else:
            currentbalance = (start_balance)
            print("Unlucky! Your current balance is now:", (currentbalance))


    if cellselect == 3:
        multiplier = 4
        while not cellselect3 in (cells):
            print("Select the cell you want to bet on.")
            try:
                cellselect3 = str(input( ))
            except ValueError:
                cellselect3 not in (cells)
            print("You selected cell:", cellselect3)
            time.sleep(1)
        print("Updated grid:")
        for n, i in enumerate(cells):
            if i == cellselect3:
                cells[n]=("o")
                grid = [cells[i:i + 5] for i in range(0, len(cells), 5)]
                for v,w,x,y,z in grid:
                    print(v,w,x,y,z)
        #User selects amount of credits to bet with.
        money_input = 0
        while not money_input in range (1, 101): #does not accept float values - will limit accuracy of balances.
            print("Enter the amount you wish to bet with:")
            try:
                money_input = int(input( ))
            except ValueError:
                money_input not in range (1, 101)
        print("You are betting",money_input,"credits on cell:",cellselect3)
        def update():
            global start_balance
            start_balance = (start_balance - money_input)
            return start_balance
        update()
        currentbalance = (start_balance)
        print("Current balance =",(currentbalance))


        #Game selects a cell. Multiplier takes effect. Money rewarded/discarded.
        print("The multiplier value is:",multiplier)
        gamerandomiser = randint(1,25)
        print ("The game selected cell:")
        gamecellselect = gridoptions[gamerandomiser]
        for n, i in enumerate(cells):
            if i == gamecellselect:
                cells[n]=("$")
                grid = [cells[i:i + 5] for i in range(0, len(cells), 5)]
                for v,w,x,y,z in grid:
                    print(v,w,x,y,z)
                
        print("Cell:",gamecellselect,"!")
        if gamecellselect == cellselect1:
            print("Congratulations, you guessed correctly.")
            print("You betted:",money_input)
            reward = (money_input * multiplier)
            print("You are rewarded with:",reward,"!")
            def update2():
                global start_balance
                start_balance = (start_balance + reward)
                return start_balance
            update()
            print("Updated balance:", (start_balance))
        else:
            currentbalance = (start_balance)
            print("Unlucky! Your current balance is now:", (currentbalance))

    if start_balance <= 0:
        print("You have run out of credits. Game Over.")
        sys.exit()
        
BetGame()

Loop = True
while Loop == True:
    restartinput = 0
    while not restartinput in ('yes','no'):
        print("Do you want to bet again? ['yes'/'no']")
        try:
            restartinput = str(input( ))
        except ValueError:
            restartinput not in ('yes','no')
        if restartinput == ('yes'):
            BetGame()
        else:
            print("Game finishes, your final balance is:", (currentbalance))
            sys.exit()
