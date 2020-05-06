import random
import os

random.seed()

# Variables

playingTheGame = True
choice = 0
gridSize = 0

shipLocation = [[int(j) for j in range(35)] for i in range(35)]
playingGrid = [[int(j) for j in range(35)] for i in range(35)]

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

# Pause Function
def pause():
    pause = input("Press any key to continue...")
    
# Build a 2 dimensional array of the size chosen
def buildGrid(gSize):
    for i in range(gSize):
        for j in range(gSize):
            playingGrid[i][j] = "  ."
                        
# Display the playing grid the size chosen
def displayGrid(gSize):
    #os.system("clear")
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
            print(playingGrid[i][j], end="")
        print(" |" + str(i+1))

def getUsersCoordinates(gSize):
    while True:
        global acrossCoord
        acrossCoord = int(input("Enter across coordinate: "))
        if acrossCoord > gSize or acrossCoord <= 0:
            print("Value must be greater than zero and less than or equal to " + str(gSize))
        else:
            break

    while True:
        global downCoord
        downCoord = int(input("Enter down coordinate: "))
        if (downCoord > gSize or downCoord <= 0):
            print("Value must be greater than zero and less than or equal to " + str(gSize))
        else:
            break

def placeShip(gSize):

    direction = random.randint(1, 4)
    limiter = random.randint(0, 5)
    gridSize = random.randint(0, gSize)
    i = 0

    while i < 4:
        if direction == 1:
            playingGrid[limiter+i][gridSize] = "  @"
            shipLocation[limiter+i][gridSize] = "  @"
        elif direction == 2:
            playingGrid[(limiter + 3) - i][gridSize] = "  @"
            shipLocation[(limiter + 3) - i][gridSize] = "  @"
        elif direction == 3:
            playingGrid[gridSize][(limiter + 3) - i] = "  @"
            shipLocation[gridSize][(limiter + 3) - i] = "  @"
        elif direction == 4:
            playingGrid[gridSize][limiter + i] = "  @"
            shipLocation[gridSize][limiter + i] = "  @"
        else:
            print("Shit done did blowed up!")
        i += 1

def calculateHit():
    hitCounter = 0

    print("P: ", end="")
    print(playingGrid[downCoord-1][acrossCoord-1])

    print("S: ", end="")
    print(shipLocation[downCoord-1][acrossCoord-1])

    if playingGrid[downCoord - 1][acrossCoord - 1] == shipLocation[downCoord - 1][acrossCoord - 1]:
        playingGrid[downCoord-1][acrossCoord-1] = "  X"
        hitCounter += 1
    else:
        playingGrid[downCoord-1][acrossCoord-1] = "  *"

    return hitCounter

def playGame(gSize):

    isItSunk = 0
    playCounter = 0

    buildGrid(gSize)
    placeShip(gSize)
    displayGrid(gSize)

    while isItSunk < 4:
        playCounter += 1

        getUsersCoordinates(gSize)

        isItSunk += calculateHit()

        displayGrid(gSize)

    print("\n\"Hey! You sunk my ship!\"")
    print("\"It took you " + str(playCounter) + " shots to sink it.\"")


# Initial game menu
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
        playGame(10)
        break
    elif str(choice) == "2":
        playGame(15)
        break
    elif str(choice) == "3":
        playGame(20)
        break
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

    pause()

