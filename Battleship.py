import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def create_board(size):
    return [["O"] * size for _ in range(size)]

def place_ship(board, size):
    ship_row = random.randint(0, size - 1)
    ship_col = random.randint(0, size - 1)
    return ship_row, ship_col

def get_guess():
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    return guess_row, guess_col

def play_battleship():
    size = 5
    board = create_board(size)
    ship_row, ship_col = place_ship(board, size)
    print("Let's play Battleship!")
    print("IMA COOK U BOI")
    print_board(board)

    for turn in range(7):
        print(f"Turn {turn + 1}")
        guess_row, guess_col = get_guess()

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row >= size) or (guess_col < 0 or guess_col >= size):
                print("Oops, that's not even in the ocean. Are you drunk?. Or maybe you're just stupid.And sped.AND BLIND")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already dummmy keep track idiot .")
            else:
                print("You missed my battleship aim u suck youre the reason the us lost the vietnam waar!")
                board[guess_row][guess_col] = "X"
            print_board(board)
        if turn == 3:
            print("Game Over")
            print(f"The ship was at ({ship_row}, {ship_col})")
            print("continue playing? Y/N")
            answer = input()
            if answer == "N":
                print("Goodbye")
                break
            else:
                print("The game will continue")
                print("The ship was at ({}, {})".format(ship_row, ship_col))

            
            
        

if __name__ == "__main__":
    play_battleship()