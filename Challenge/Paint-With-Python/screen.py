import pygame
import sys

pygame.init()

# Set up the Pygame window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Paint Program')

# Set up the drawing surface
drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_surface.fill((255, 255, 255))

# Set up colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

# Set the default color
color = BLACK

# Set the default brush size
brush_size = 7

# Function to draw on the screen
def draw(pos):
    pygame.draw.circle(drawing_surface, color, pos, brush_size)

# Function to set the color
def set_color(c):
    global color
    color = c

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Get the position of the mouse when the left button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

        # Draw on the screen when the left mouse button is pressed and moved
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            draw(pygame.mouse.get_pos())

        # Set the color based on keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                set_color(BLACK)
            elif event.key == pygame.K_2:
                set_color(RED)
            elif event.key == pygame.K_3:
                set_color(GREEN)
            elif event.key == pygame.K_4:
                set_color(BLUE)
            elif event.key == pygame.K_5:
                set_color(YELLOW)
            elif event.key == pygame.K_6:
                set_color(PURPLE)

    # Draw the drawing surface on the screen
    screen.blit(drawing_surface, (0, 0))

    # Update the Pygame window
    pygame.display.update()

