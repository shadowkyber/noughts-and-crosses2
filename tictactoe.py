# displays grid
def display(g):
    print("---------")
    print("|", g[0][0], g[0][1], g[0][2], "|")
    print("|", g[1][0], g[1][1], g[1][2], "|")
    print("|", g[2][0], g[2][1], g[2][2], "|")
    print("---------")


# checks if anyone has won
def winner():
    c = 0  # count of empty spaces
    die1 = []
    for hor in range(3):
        column = []
        c += grid[hor].count(" ")  # check grid's not full
        die1.append(grid[hor][hor])  # list of cords 11, 22, 33
        if grid[hor].count(grid[hor][0]) == 3:  # checks if anyone has won in horizontally
            return grid[hor][0]

        for ver in range(3):
            column.append(grid[ver][hor])  # list of vertical, columns
        if column.count(column[0]) == 3:  # checks if anyone has won vertically
            return column[0]

    if grid[0][2] == grid[1][1] == grid[2][0]:  # checks if anyone has won diagonally, right to left
        return grid[0][2]

    if die1.count(die1[0]) == 3:  # checks if anyone has won diagonally, left to right
        return die1[0]

    if c == 0:  # if grid is full
        return "draw"


# checks if coordinates are fine
def check(_x, _y):
    try:  # check cords are good
        _x = int(_x)-1
        _y = int(_y)-1
        if not -1 < _x < 3 or not -1 < _y < 3:  # check cords are between 1 and 3
            print("Coordinates should be from 1 to 3!")
            return True
        elif grid[_x][_y] != " ":  # check cords are empty
            print("This cell is occupied! Choose another one!")
            return True
        else:
            return False
    except ValueError:  # check cords are numbers
        print("You should enter numbers!")
        return True


# creates empty grid
grid = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

turn = 0
while True:  # game
    display(grid)  # display grid
    w = winner()  # check for winner or tie

    # says who has won and ends game
    if w == "X":
        print("X wins")
        break
    elif w == "O":
        print("O wins")
        break
    elif w == "draw":
        print("Draw")
        break

    # gets cords and checks if they are good
    x, y = input("Enter the coordinates: ").split()
    bad = check(x, y)
    while bad:
        x, y = input("Enter the coordinates: ").split()
        bad = check(x, y)

    x = int(x) - 1
    y = int(y) - 1

    if turn % 2 == 0:  # decides who's turn it it
        w = "X"
    else:
        w = "O"

    grid[x][y] = w  # update grid

    turn += 1  # change turn
