#! /usr/bin/python3

# --- deminor.py --- #

'''This project is a miner game, you have a board of size n * n, there are bombs in it and the goal is to dig all
the coordinates not filled with bombs, good luck pal !'''

import random

MINE = 'B'

def create_board(size):
    board = []
    for i in range(size):
        board.append(["."] * size)
    return (board)

def is_input_numeric(n):
    if n.isnumeric() == True:
        return (True)
    else:
        print("\nYour input should be a number")
        return (False)

def display_board(board, size):
    coordinates = []
    for i in range(1, size + 1):
        coordinates.append(str(i))
    print("\n", " " * 12, '   '.join(coordinates))
    print(" " * 11, "----" * size + "-")
    for i in range(size):
        print(" " * 8, "|")
        print(" " * 6, i + 1, "|   " ,'   '.join(board[i]))

def place_mines(board, size):
    while True:
        print("\nHow many mines maximum do you want (have to be less than", size * size, ") ?")
        mines = input()
        if is_input_numeric(mines) == False:
            continue
        mines = int(mines)
        if mines <= 0:
            print("\nCome on cowards, let's have some chalenge would you ?")
            continue
        if mines >= size * size:
            print("Too many mines")
        else:
            while mines > 0:
                board[random.randint(0, size - 1)][random.randint(0, size - 1)] = MINE
                mines -= 1
            return (board)

def check_mines(board, i, j, size):
    '''Childish implementation of an algorithm to check the 8 surrounding coordinates around a position to fill
    it with the number of bombs around (bad optimisation)'''
    num_mines = 0
    if i > 0:
        if board[i - 1][j] == MINE:         #haut
            num_mines += 1
        if j > 0:
            if board[i - 1][j - 1] == MINE: #haut a gauche
                num_mines += 1
        if j < size - 1:
            if board[i - 1][j + 1] == MINE: #haut a droite
                num_mines += 1
    if j > 0:
        if board[i][j - 1] == MINE:         #gauche
            num_mines += 1
    if j < size - 1:
        if board[i][j + 1] == MINE:         #droite
            num_mines += 1
    if i < size - 1:
        if board[i + 1][j] == MINE:         #bas
            num_mines += 1
        if j > 0:
            if board[i + 1][j - 1] == MINE: #bas a gauche
                num_mines += 1
        if j < size - 1:
            if board[i + 1][j + 1] == MINE: #bas a droite
                num_mines += 1
    return (str(num_mines))

def proper_board(board, size):
    for i in range(size):
        for j in range(size):
            if board[i][j] != MINE:
                board[i][j] = check_mines(board, i, j, size)
    return (board)

def dig_left(board, size):
    total = 0
    for i in range (size):
        for j in range (size):
            if board[i][j] == MINE:
                total += 1
    return ((size * size) - total)

def play(board, size):
    display = create_board(size)
    res = 0
    dig = dig_left(board, size)
    while res == 0:
        display_board(display, size)
        while True:
            line = input("Choose the line you want to dig : ")
            column = input("Choose the column you want to dig : ")
            if is_input_numeric(line) == True and is_input_numeric(column) == True:
                line = int(line) - 1
                column = int(column) - 1
                if line < 0 or line >= size or column < 0 or column >= size:
                    print("\nPlease enter valid coordinates\n")
                else:
                    break
        if display[line][column] == ".":
            dig -= 1
        display[line][column] = board[line][column]
        if board[line][column] == MINE:
            display_board(display, size)
            print("\nOh oh... there was a mine there")
            res = 2
            break
        if dig == 0:
            display_board(board, size)
            res = 1
    if res == 1:
        print("\nCongratulation, you did it !")
    if res == 2:
        print("\nYou lose...\nTry again !\n")

def game():
    while True:
        size = input("\nChoose the size of your board (size * size board) : ")
        if is_input_numeric(size) == False:
            continue
        size = int(size)
        if size <= 0:
            print("\nYou can't have a board of size 0")
            continue
        board = create_board(size)
        display_board(board, size)
        test = input("\nIs the size correct for your game ? (y/n) : ")
        while test != 'y' and test != 'n' and test != 'yes' and test != 'no':
            print("\nUnknown command\n")
            test = input("Is the size correct for your game ? (y/n) : ")
        if test == 'y' or test == 'yes':
            break
        if test == 'n' or test == 'no':
            continue
    board = place_mines(board, size)
    #display_board(board, size) #Comment this line for hiding mines location
    board = proper_board(board, size)
    #display_board(board, size) #Comment this line for hiding mines location
    print("\nLet's go !\n")
    play(board, size)

print("\nWelcome to the Miner game !\n\n")
while True:
    choice = input("For starting a new game please type \"game\" and press <enter> , q to exit the game : ")
    if choice == "q" or choice == "quit" or choice == "exit":
        print("\nGood bye, see you soon !\n")
        break
    elif choice == "game":
        game()
    else:
        print("\nUnknown command\n")
