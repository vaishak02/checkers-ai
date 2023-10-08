import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (128, 0, 32)
ALMOND = (234, 221, 202)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (44, 25))
