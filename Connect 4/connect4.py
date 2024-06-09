import numpy as np
import pygame
import sys
import math
import random

ROW_NUMBER = 6
COLUMN_NUMBER = 7

PLAYER = 0
AI = 1

PLAYER_PIECE = 1
AI_PIECE = 2

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


def create_board():
    board = np.zeros((ROW_NUMBER, COLUMN_NUMBER))  # matrix
    return board


def display_board(board):
    print(np.flip(board, 0))  # Flipping the board upside down for correct orientation


def draw_board(board):
    for row in range(ROW_NUMBER):
        for col in range(COLUMN_NUMBER):
            pygame.draw.rect(
                screen,
                BLUE,
                (
                    col * SQUARE_SIZE,
                    row * SQUARE_SIZE + SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE,
                ),
            )
            pygame.draw.circle(
                screen,
                BLACK,
                (
                    int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                    int(row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2),
                ),
                RADIUS,
            )

    for row in range(ROW_NUMBER):
        for col in range(COLUMN_NUMBER):
            if board[row][col] == PLAYER_PIECE:
                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                        screen_height - int(row * SQUARE_SIZE + SQUARE_SIZE / 2),
                    ),
                    RADIUS,
                )
            elif board[row][col] == AI_PIECE:
                pygame.draw.circle(
                    screen,
                    YELLOW,
                    (
                        int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                        screen_height - int(row * SQUARE_SIZE + SQUARE_SIZE / 2),
                    ),
                    RADIUS,
                )
    pygame.display.update()


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid(board, col):
    return board[ROW_NUMBER - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_NUMBER):
        if board[r][col] == 0:
            return r


def check_win(board, piece):
    # Checking Horizontal
    for row in range(ROW_NUMBER):
        for col in range(COLUMN_NUMBER - 3):
            if (
                board[row][col] == piece
                and board[row][col + 1] == piece
                and board[row][col + 2] == piece
                and board[row][col + 3] == piece
            ):
                return True
    # Checking Verticle
    for row in range(ROW_NUMBER - 3):
        for col in range(COLUMN_NUMBER):
            if (
                board[row][col] == piece
                and board[row + 1][col] == piece
                and board[row + 2][col] == piece
                and board[row + 3][col] == piece
            ):
                return True
    # Checking Diagonal (Positively Sloped)
    for row in range(ROW_NUMBER - 3):
        for col in range(COLUMN_NUMBER - 3):
            if (
                board[row][col] == piece
                and board[row + 1][col + 1] == piece
                and board[row + 2][col + 2] == piece
                and board[row + 3][col + 3] == piece
            ):
                return True

    # Checking Diagonal (Ngeatively Sloped)
    for row in range(3, ROW_NUMBER):
        for col in range(COLUMN_NUMBER - 3):
            if (
                board[row][col] == piece
                and board[row - 1][col + 1] == piece
                and board[row - 2][col + 2] == piece
                and board[row - 3][col + 3] == piece
            ):
                return True


def score_position(board, piece):
    # Horizontal Score
    pass


board = create_board()
display_board(board)
game_over = False

pygame.init()

SQUARE_SIZE = 100  # Pixels

screen_width = COLUMN_NUMBER * SQUARE_SIZE
screen_height = (ROW_NUMBER + 1) * SQUARE_SIZE  # Extra Row for the space to drop

screen_size = (screen_width, screen_height)

RADIUS = int(SQUARE_SIZE / 2 - 5)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Connect 4 AI")
draw_board(board)
pygame.display.update()
# pygame.font.get_fonts()
myFont = pygame.font.SysFont("monospace", 75, bold=True)

turn = random.randint(PLAYER, AI)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, screen_width, SQUARE_SIZE))
            posX = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, RED, (posX, int(SQUARE_SIZE / 2)), RADIUS)
            # else:
            #     pygame.draw.circle(screen, YELLOW, (posX, int(SQUARE_SIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, screen_width, SQUARE_SIZE))
            # Ask for Player 1 input
            if turn == PLAYER:
                posX = event.pos[0]  # Between 0 and 700; x axis position
                col = int(math.floor(posX / SQUARE_SIZE))

                if is_valid(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_PIECE)

                    if check_win(board, 1):
                        # pygame.draw.rect(
                        #     screen, BLACK, (0, 0, screen_width, SQUARE_SIZE)
                        # )
                        label = myFont.render("Player 1 Wins!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

                    turn += 1
                    turn = turn % 2

                    # display_board(board)
                    draw_board(board)

                # Ask for Player 2 input
                # else:

                # posX = event.pos[0]  # Between 0 and 700
                # col = int(math.floor(posX / SQUARE_SIZE))

                # if is_valid(board, col):
                #     row = get_next_open_row(board, col)
                #     drop_piece(board, row, col, 2)
                #     if check_win(board, 2):
                #         pygame.draw.rect(
                #                     screen, BLACK, (0, 0, screen_width, SQUARE_SIZE)
                #                 )
                #         label = myFont.render("Player 2 Wins!", 1, RED)
                #         screen.blit(label, (40, 10))
                #         game_over = True
                #     draw_board(board)

    # AI turn

    if turn == AI and not game_over:

        col = random.randint(0, COLUMN_NUMBER - 1)

        if is_valid(board, col):
            pygame.time.wait(500)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)
            if check_win(board, 2):
                label = myFont.render("Player 2 Wins!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True
            draw_board(board)
            # display_board(board)

            turn += 1
            turn = turn % 2

    if game_over:
        pygame.time.wait(3000)
