import pygame, sys, random

# sys to manage some of the functionaity in your system

# General Setup
pygame.init()  # initiaziling pygame
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode(
    (screen_width, screen_height)
)  # can take number of parameters of more complex game
pygame.display.set_caption("Pong")

while True:
    # Handling Input
    for (
        event
    ) in (
        pygame.event.get()
    ):  # list of all user inputs, calls all user interactions as events
        if event.type == pygame.QUIT:
            pygame.quit()  # Quitting the window
            sys.exit()

    # Updating the window
    pygame.display.flip()  # Draw a picture from the loop
    clock.tick(60)  # Limits the time of the loop
