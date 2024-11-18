
import random
from collections import deque

BOARD_SIZE = 10
SHIP_SIZES = [5, 4, 3, 3, 2] 

def create_board():
    
    return [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]

def print_board(board, hide_ships=False):
    
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        row_display = []
        for cell in row:
            if cell == "S" and hide_ships:
                row_display.append("~")
            else:
                row_display.append(cell)
        print(f"{i} " + " ".join(row_display))

#Placing Ships on the Board
#This part contains functions to place ships randomly on the boards.
def place_ship(board, ship_size):
    #Randomly placing a ship of a given size on the board.
    while True:
        orientation = random.choice(["horizontal", "vertical"])
        if orientation == "horizontal":
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - ship_size)
            if all(board[row][col + i] == "~" for i in range(ship_size)):
                for i in range(ship_size):
                    board[row][col + i] = "S"
                break
        else:
            row = random.randint(0, BOARD_SIZE - ship_size)
            col = random.randint(0, BOARD_SIZE - 1)
            if all(board[row + i][col] == "~" for i in range(ship_size)):
                for i in range(ship_size):
                    board[row + i][col] = "S"
                break

def setup_game():
    #Seting up the game boards for both player and AI by placing ships.
    player_board = create_board()
    ai_board = create_board()
    
    for ship_size in SHIP_SIZES:
        place_ship(player_board, ship_size)
        place_ship(ai_board, ship_size)
    
    return player_board, ai_board
#Player's Turn
#This part contains code for the player’s move input and marking hits/misses on the AI’s board.
def player_move(board):
    #Geting player's shot coordinates and validate input.
    while True:
        try:
            row = int(input("Enter row (0-9): "))
            col = int(input("Enter col (0-9): "))
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                if board[row][col] == "~" or board[row][col] == "S":
                    return row, col
                else:
                    print("You already shot there. Try again.")
            else:
                print("Out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

def check_hit(board, row, col):
    #Check if the shot is a hit or miss.
    if board[row][col] == "S":
        board[row][col] = "X"  # Mark as hit
        return True
    board[row][col] = "O"  # Mark as miss
    return False