

#import items from numpy library
#create a function that takes a parameter and generates a board and assign one of the strings to each cell on board
#create function that will return the sum of the board and item to get total number of items that exist on board
#check to see if this file is running in main

from numpy import random

def build_board(size):
    cell_values=['Empty', 'Red', 'Black']

    board=random.choice(cell_values, size=(size, size))
    return board

def get_count(board, item):
    return (board==item).sum()

if __name__ == "__main__":
    print("This file is not intended to be run as a main.")