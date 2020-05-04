import random

random.seed()

# Variables

shipLocation = 0
acrossCoord = 0
downCoord = 0
playingTheGame = True
choice = 0
gridSize = 0

displayHelpInfo = """
The object of the game is to sink the ship.  There will be one ship 
on the grid.  The player will choose horizontal and virtical coordinates 
and the game will calculate whether those coordiantes were a hit or a 
miss.  An \"X\" will mark a hit and \"*\" a miss.  The difficulty levels 
will be set as so; "

\tEasy will be a grid of 10 x 10
\tNormal will be a grid of 15 x 15
\tHard will be a grid of 20 x 20

You may exit the game at any time by hitting \"Ctrl-C\".
"""

# Functions
def pause():
    pause = input("Press any key to continue...")
    
def buildGrid(gSize):
    for x in range(gSize):
        if x < 10:
            print("  " + str(x+1), end="")
        else:
            print(" " + str(x+1), end="")
    print()
    
    for y in range(gSize):
        if y < 10:
            print("---", end="")
        else:
            print("---", end="")
        if y == gSize - 1:
            print("-\\")

    for i in range(gSize):
        for j in range(gSize):
            print("  .", end="")
        print(" |" + str(i+1))

# Main game loop
while playingTheGame:
    print("Please make a selection:")
    print("1 - Easy")
    print("2 - Normal")
    print("3 - Hard")
    print()
    print("H - Help")
    print("Q - Quit")
    print("-------------------------")
    choice = input("Enter your choice: ")

    if str(choice) == "1":
#        print("Easy")
        gridSize = 10
    elif str(choice) == "2":
#        print("Normal")
        gridSize = 15
    elif str(choice) == "3":
#        print("Hard")
        gridSize = 20
    elif str(choice) == "H" or str(choice) == "h":
        print(displayHelpInfo)
        gridSize = 0
        pause()
    elif str(choice) == "Q" or str(choice) == "q":
        playingTheGame = False
        print("\n\nThank you for playing.")
        print("Goodbye.\n")
        break
    else:
        print("Error")

    buildGrid(gridSize)

    print("Enter across coordinate")
    print("Enter down coordinate")

    pause()

