import os
import random
import time

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
winner = None
currentPlayer = "X"
gameRunning = True


# Clears the console screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Displaying Board
def displayBoard(board):
    """
    Displays the board
    """
    print("-" * 17)
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("-" * 17)
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("-" * 17)
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8])
    print("-" * 17)


# Player Input


def playerInput(currentPlayer):
    while True:
        position = int(input("Choose your position! Enter a number between 1-9: "))
        if position not in range(1, 10) or board[position - 1] != "-":
            print("Invalid postion! Please enter a valid postion.")
        elif board[position - 1] == "-":
            board[position - 1] = currentPlayer
            return False


# Checking for win or tie


def checkHorizontle(board):
    global winner
    if (
        (board[0] == board[1] == board[2] and board[0] != "-")
        or (board[3] == board[4] == board[5] and board[3] != "-")
        or (board[6] == board[7] == board[8] and board[6] != "-")
    ):
        winner = currentPlayer
        return True
    # if board[0] == board[1] == board[2] and board[0] != "-":
    #     winner = board[0]
    #     return True
    # elif board[3] == board[4] == board[5] and board[3] != "-":
    #     winner = board[3]
    #     return True
    # elif board[6] == board[7] == board[8] and board[0] != "-":
    #     winner = board[6]
    #     return True


def checkVerticle(board):
    global winner
    if (
        (board[0] == board[3] == board[6] and board[0] != "-")
        or (board[1] == board[4] == board[7] and board[1] != "-")
        or (board[2] == board[5] == board[8] and board[2] != "-")
    ):
        winner = currentPlayer
        return True
    # if board[0] == board[3] == board[6] and board[0] != "-":
    #     winner = board[0]
    #     return True
    # elif board[1] == board[4] == board[7] and board[1] != "-":
    #     winner = board[1]
    #     return True
    # elif board[2] == board[5] == board[8] and board[2] != "-":
    #     winner = board[2]
    #     return True


def checkDiag(board):
    global winner
    if (board[0] == board[4] == board[8] and board[4] != "-") or (
        board[2] == board[4] == board[6] and board[4] != "-"
    ):
        winner = currentPlayer
        return True
    # if board[0] == board[4] == board[8] and board[4] != "-":
    #     winner = board[0]
    #     return True
    # elif board[2] == board[4] == board[6] and board[4] != "-":
    #     winner = board[2]
    #     return True


def checkTie(board):

    global gameRunning
    if "-" not in board:
        displayBoard(board)
        print("It's a tie!")
        gameRunning = False


def checkWin():
    global gameRunning
    if checkDiag(board) or checkHorizontle(board) or checkVerticle(board):
        displayBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False


# Switch players
def switchPlayers():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayers()


def main():
    while gameRunning:
        displayBoard(board)
        print(f"It's {currentPlayer}'s turn! Please make a move.")
        playerInput(currentPlayer)
        clear_screen()
        checkWin()
        checkTie(board)
        switchPlayers()
        computer(board)
        checkWin()
        checkTie(board)
        # switchPlayers()


main()
