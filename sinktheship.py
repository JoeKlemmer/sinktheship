import random
import os

random.seed()

# Variables

playingTheGame = True
choice = 0
gridsize = 0

shipLocation = [[int(j) for j in range(35)] for _ in range(35)]
playingGrid = [[int(j) for j in range(35)] for _ in range(35)]

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
def build_grid(gsize):
    for i in range(gsize):
        for j in range(gsize):
            playingGrid[i][j] = "  ."
                        
# Display the playing grid the size chosen
def display_grid(gsize):
    # os.system("clear")
    for x in range(gsize):
        if x < 10:
            print("  " + str(x+1), end="")
        else:
            print(" " + str(x+1), end="")
    print()
    
    for y in range(gsize):
        if y == 0:
            print(" --", end="")
        else:
            print("---", end="")

        if y == gsize - 1:
            print("-\\")

    for i in range(gsize):
        for j in range(gsize):
            print(playingGrid[i][j], end="")
        print(" |" + str(i+1))

def get_users_coordinates(gsize):
    while True:
        try:
            global acrossCoord
            acrossCoord = int(input("Enter across coordinate: "))
        except ValueError:
            print("Value must be a number")
        else:
            if acrossCoord > gsize or acrossCoord <= 0:
                print("Value must be greater than zero and less than or equal to " + str(gsize))
            else:
                break

    while True:
        try:
            global downCoord
            downCoord = int(input("Enter down coordinate: "))
        except ValueError:
            print("Value must be a number")
        else:
            if (downCoord > gsize or downCoord <= 0):
                print("Value must be greater than zero and less than or equal to " + str(gsize))
            else:
                break

def place_ship(gsize):

    direction = random.randint(1, 4)
    limiter = random.randint(0, 5)
    gridsize = random.randint(0, (gsize - 1))
    i = 0

    while i < 4:
        if direction == 1:  # North
            print("N" + str(limiter+i) + "x" + str(gridsize))
            playingGrid[limiter+i][gridsize] = "  @"
            shipLocation[limiter+i][gridsize] = "  @"
        elif direction == 2:    #South
            print("S" + str(limiter + 3) - i + "x" + str(gridsize))
            playingGrid[(limiter + 3) - i][gridsize] = "  @"
            shipLocation[(limiter + 3) - i][gridsize] = "  @"
        elif direction == 3:    #East
            print("E" + str(gridsize) + "x" + str((limiter + 3) - i))
            playingGrid[gridsize][(limiter + 3) - i] = "  @"
            shipLocation[gridsize][(limiter + 3) - i] = "  @"
        elif direction == 4:    #West
            print("W" + str(gridsize) + "x" + str(limiter + i))
            playingGrid[gridsize][limiter + i] = "  @"
            shipLocation[gridsize][limiter + i] = "  @"
        else:
            print("Shit done did blowed up!")
        i += 1

def calculate_hit():
    hit_counter = 0

    print("P: ", end="")
    print(playingGrid[downCoord-1][acrossCoord-1])

    print("S: ", end="")
    print(shipLocation[downCoord-1][acrossCoord-1])

    if playingGrid[downCoord - 1][acrossCoord - 1] == shipLocation[downCoord - 1][acrossCoord - 1]:
        playingGrid[downCoord-1][acrossCoord-1] = "  X"
        hit_counter += 1
    else:
        playingGrid[downCoord-1][acrossCoord-1] = "  *"

    return hit_counter

def play_game(gsize):

    is_is_sunk = 0
    play_counter = 0

    build_grid(gsize)
    place_ship(gsize)
    display_grid(gsize)

    while is_is_sunk < 4:
        play_counter += 1

        get_users_coordinates(gsize)

        is_is_sunk += calculate_hit()

        display_grid(gsize)

    print("\n\"Hey! You sunk my ship!\"")
    print("\"It took you " + str(play_counter) + " shots to sink it.\"")


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
        play_game(10)
        break
    elif str(choice) == "2":
        play_game(15)
        break
    elif str(choice) == "3":
        play_game(20)
        break
    elif str(choice) == "H" or str(choice) == "h":
        print(displayHelpInfo)
        gridsize = 0
        pause()
    elif str(choice) == "Q" or str(choice) == "q":
        playingTheGame = False
        print("\n\nThank you for playing.")
        print("Goodbye.\n")
        break
    else:
        print("Error")

    pause()

