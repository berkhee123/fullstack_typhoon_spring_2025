import pygame
import sys

# Initialize Pygame / Pygame ehluuleh
pygame.init()

# Set up the display / Delgets tohiruulah 
WIDTH = 800 
HEIGHT = 600 
screen = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window")

# Define colors (R, G, B) / Ongo todorhoiloh
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game loop / Togloomiin davtalt 
clock = pygame.time.Clock()
running = True

while running:
    # Handle events / Uildluud bolovsruulah 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen / Delgets duurgeh
    screen.fill(WHITE)

    # Draw here / End darah 
    pygame.draw.circle(screen, RED, (400, 300), 50)

    # Update the display / Delgets shinechleh
    pygame.display.flip()
    clock.tick(60) # 60 FPS

# QUIT / Garah 
pygame.quit()
sys.exit()