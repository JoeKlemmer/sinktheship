import random
import os

random.seed()

# Variables

playing_the_game = True

ship_location = [[int(j) for j in range(25)] for _ in range(25)]
playing_grid = [[int(j) for j in range(25)] for _ in range(25)]

display_help_info = """
The object of the game is to sink the ship.  There will be one ship 
on the grid.  The player will choose horizontal and virtical coordinates 
and the game will calculate whether those coordiantes were a hit or a 
miss.  An \"X\" will mark a hit and \"*\" a miss.  The difficulty levels 
will be set as follows;

 - Easy will be a grid of 10 x 10
 - Normal will be a grid of 15 x 15
 - Hard will be a grid of 20 x 20

You will have 15, 20, and 25 attempts, respectively, to sink the ship.
If you do not, the ship will escape and you lose.

You may exit the game at any time by hitting \"Ctrl-C\".
"""

# Build a 2 dimensional array of the size chosen
def build_grid(gsize):
    for i in range(gsize):
        for j in range(gsize):
            playing_grid[i][j] = "  ."

# Display the playing grid the size chosen
def display_grid(gsize):
    os.system("clear")
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
            print(playing_grid[i][j], end="")
        print(" |" + str(i+1))

# Get the users coordinates
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

# Determin where and in what doirecton to place the ship
def place_ship(gsize):

    direction = random.randint(1, 4)

    # The limiter keeps the ship from being placed outside the grid
    limiter = random.randint(0, 5)
    gridsize = random.randint(0, (gsize - 1))
    i = 0

    while i < 4:
        if direction == 1:  # North
           # playing_grid[limiter+i][gridsize] = "  @"    # <-- Used for debugging
           ship_location[limiter+i][gridsize] = "  @"
        elif direction == 2:    #South
           # playing_grid[(limiter + 3) - i][gridsize] = "  @"    # <-- Used for debugging
           ship_location[(limiter + 3) - i][gridsize] = "  @"
        elif direction == 3:    #East
           # playing_grid[gridsize][(limiter + 3) - i] = "  @"    # <-- Used for debugging
           ship_location[gridsize][(limiter + 3) - i] = "  @"
        elif direction == 4:    #West
           # playing_grid[gridsize][limiter + i] = "  @"    # <-- Used for debugging
           ship_location[gridsize][limiter + i] = "  @"
        else:
            # If we end up here, something broke
            print("Shit done did blowed up!")
        i += 1

# CHeck to see if the coordinates the user entered hit the ship
def calculate_hit():
    hit_counter = 0

    if playing_grid[downCoord - 1][acrossCoord - 1] == ship_location[downCoord - 1][acrossCoord - 1]:
        playing_grid[downCoord-1][acrossCoord-1] = "  X"
        hit_counter += 1
    else:
        playing_grid[downCoord-1][acrossCoord-1] = "  *"

    return hit_counter

# Basically, the main game loop
def play_game(gsize):

    is_it_sunk = 0
    play_counter = 0

    build_grid(gsize)
    place_ship(gsize)
    display_grid(gsize)

    while is_it_sunk < 4 and play_counter < gsize + 5:
        play_counter += 1

        print("You have " + str((gsize + 6) - play_counter) + " attempts left")

        get_users_coordinates(gsize)

        is_it_sunk += calculate_hit()

        display_grid(gsize)
        
    if is_it_sunk == 4:
        print("\n\"Hey! You sunk my ship!\"")
        print("\"It took you " + str(play_counter) + " shots to sink it.\"")
    else:
        print("\n\"Ha! You took too long. I got away!\"")
        print("Better luck next time.")

# Initial game menu
print("\nGreetings Professor Falken.")
print("Welcome to \"Sink My Ship\"")

while playing_the_game:
    print("\nPlease make a selection:")
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
        print(display_help_info)
    elif str(choice) == "Q" or str(choice) == "q":
        playing_the_game = False
        print("\n\nThank you for playing.")
        print("Goodbye.\n")
        break
    else:
        print("\nError: You must enter one of the above options\n")

    pause = input("Press any key to continue...")

