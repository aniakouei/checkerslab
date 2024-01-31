#import other file
#create game function that allows user to input size of board
    #use checkers functions to print how many red, black, and empty cells
#call function
from checkerslab import checkers


def game():
    size=int(input("Enter the size of the board: "))
    board= checkers.build_board(size)

    print("Board: ")
    print(board)

    print("Count of Empty cells:", checkers.get_count(board, 'Empty'))
    print("Count of Red cells:", checkers.get_count(board, 'Red'))
    print("Count of Black cells:", checkers.get_count(board, 'Black'))

game()