# Menu so that the player can select play with or without rotation.
def menu():
    print("============MENU=============")
    print("1.Play Without Rotation.")
    print("2.Play with Rotation.")

    # Exceptional value errors for choice
    ex_loop = True
    while ex_loop:
        try:
            cho = int(input("Enter 1 or 2 as per your choice."))

            if cho == 1:
                ex_loop = False
                play_without_rot()
            elif cho == 2:
                ex_loop = False
                play_with_rot()
            else:
                print("Invalid Integer. Enter 1 or 2.")

        except ValueError:
            print("Input not an integer.")


# Initial function to play without rotation
def play_without_rot():
    global player
    global check
    global loop
    create_grid()

    check = []

    player = 1

    # Game loop
    loop = True

    while loop:
        loop_num = check_win()
        if loop_num != 0:
            loop = False
        if not loop:
            break
        column_input()
        piece_placement()
        checker()
        switch_turn()

    display_grid()


# Initial function to play with rotation
def play_with_rot():
    global player
    global check
    global loop
    create_grid()

    check = []

    player = 1

    # Game loop
    loop = True
    while loop:
        loop_num = check_win()
        if loop_num != 0:
            loop = False
        if not loop:
            break
        column_input()
        piece_placement()
        checker()
        switch_turn()

        # Exceptional value errors for number of rotations (0 to 3)
        ex_loop = True
        while ex_loop:
            try:
                rotate = int(input("How many times do you want to rotate the grid (1 to 3) or 0 for no rotation? "))

                if 0 < rotate < 4:
                    ex_loop = False
                    rotate_grid_clockwise(rotate)
                elif rotate == 0:
                    ex_loop = False
                else:
                    print("Invalid Integer. Enter number between 0 to 3!!!")

            except ValueError:
                print("Input not an integer.")

    display_grid()


# Initialization of n*n grid
def create_grid():
    global n

    # Exceptional value errors for grid size (>= 4)
    ex_loop = True
    while ex_loop:
        try:
            n = int(input("Enter grid size greater or equal to 4 (N * N matrix) : "))

            if n > 3:
                ex_loop = False
            else:
                print("Enter matrix size greater than or equal to 4")

        except ValueError:
            print("Input not an integer")

    global grids
    grids = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            grids[i].append(j)
            grids[i][j] = - 1
    display_grid()


# Displays the current state of the grid
def display_grid():
    # Create temp board for display
    board = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            board[i].append(j)
            board[i][j] = "   "

    for i in range(n):
        for j in range(n):
            if grids[i][j] == 1:
                board[i][j] = " X "
            elif grids[i][j] == 2:
                board[i][j] = " O "

    # To display the temp board to the player
    e = "\n", "--- " * n, "\n"
    print(("".join(str(i) for i in e).join("|".join(str(x) for x in row) for row in board)))


# To ask current player piece placement column
def column_input():
    # Exceptional value error for user_input
    loop_2 = True
    while loop_2:
        try:
            global user_input
            user_input = int(input("\nInput a column player " + str(player) + " from 1 to " + str(n) + ":\n"))

            if (n + 1) > user_input > 0:
                loop_2 = False
            else:
                print("Invalid integer value")
        except ValueError:
            print("Invalid Input")


# Player piece is placed if column has empty space
# Else asks another input
def piece_placement():
    for i in range(n - 1, -1, -1):
        full = column_full()
        if full == -1:
            print("Slot is full try again!!!")
            column_input()
            piece_placement()
            break
        elif full == 0:
            if grids[i][user_input - 1] == -1:
                if player == 1:
                    grids[i][user_input - 1] = 1
                elif player == 2:
                    grids[i][user_input - 1] = 2
                display_grid()
                break


# Calls check_win
# If winner found prints and calls play_again
def checker():
    winner = check_win()
    if winner == 0:
        full = column_full()
        if full == -1:
            print("Now this column is full")
    else:
        print("Player " + str(player) + " has won!!! Congrats!!!")
        play_again()


# checks if there is a winner
def check_win():

    # check horizontal spaces
    for x in range(n):
        for y in range(n - 3):
            if grids[x][y] != -1 and grids[x][y + 1] == grids[x][y] and grids[x][y + 2] == grids[x][y] and grids[x][y + 3] == grids[x][y]:
                return player

    # check vertical spaces
    for y in range(n):
        for x in range(n - 3):
            if grids[x][y] != -1 and grids[x + 1][y] == grids[x][y] and grids[x + 2][y] == grids[x][y] and grids[x + 3][y] == grids[x][y]:
                return player

    # check / diagonal spaces
    for x in range(n - 3):
        for y in range(3, n):
            if grids[x][y] != -1 and grids[x + 1][y - 1] == grids[x][y] and grids[x + 2][y - 2] == grids[x][y] and grids[x + 3][y - 3] == grids[x][y]:
                return player

    # check \ diagonal spaces
    for x in range(n - 3):
        for y in range(n - 3):
            if grids[x][y] != -1 and grids[x + 1][y + 1] == grids[x][y] and grids[x + 2][y + 2] == grids[x][y] and grids[x + 3][y + 3] == grids[x][y]:
                return player

    return 0


# Switches current player
def switch_turn():
    global player
    player = 2 if player < 2 else 1


# Checks if the column is full
def column_full():
    if grids[0][user_input - 1] == -1:
        return 0

    complete_board_full()
    return -1


# Checks if the whole grid is full
def complete_board_full():
    count = sum(grids[0][i] != -1 for i in range(n))
    if count == n:
        print("The complete board is full,\n The game is a Tie.")
        play_again()

1
# Rotates the grid 90 degrees clockwise
def rotate_grid_clockwise(k):
    for _ in range(k):
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = grids[i][j]
                grids[i][j] = grids[n - 1 - j][i]
                grids[n - 1 - j][i] = grids[n - 1 - i][n - 1 - j]
                grids[n - 1 - i][n - 1 - j] = grids[j][n - 1 - i]
                grids[j][n - 1 - i] = temp
    display_grid()
    gravity()


# Pieces are rearranged after rotation
def gravity():
    print("After rotation: ")
    for _ in range(n):
        for i in range(n - 1):
            for j in range(n):
                if grids[i + 1][j] == -1:
                    grids[i + 1][j] = grids[i][j]
                    grids[i][j] = -1
    display_grid()


# Enables to play the game again
def play_again():
    # Exceptional value error for play again input
    ex_loop = True
    while ex_loop:
        try:
            ch = input("Do you want to play again??(Y/N)")

            if ch.upper() in ["YES", 'Y']:
                ex_loop = False
                menu()
            elif ch.upper() in ["NO", 'N']:
                ex_loop = False
                print("Thank You!!!")
                input("Enter any key to exit")
                exit()
            else:
                print("Invalid try again!!!")
                play_again()

        except ValueError:
            print("Invalid Input")


menu()
