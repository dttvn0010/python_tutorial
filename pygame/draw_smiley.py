import pygame, sys

BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))
screen.fill(WHITE)

# Face
pygame.draw.circle(screen, YELLOW, (320, 240),  70, 0)
pygame.draw.circle(screen, BLACK, (320, 240),  70, 2)

# Eyes
pygame.draw.circle(screen, BLACK, (295, 220),  10)
pygame.draw.circle(screen, BLACK, (345, 220),  10)

# Mouth
rect = pygame.Rect(270, 190, 100, 100)
pygame.draw.arc(screen, BLACK, rect, -3, -0.1, 3)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
