import pygame, sys

WHITE = 255, 255, 255
GREEN = 0, 255, 0
YELLOW = 255, 255, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

screen.fill(WHITE)

pygame.draw.polygon(screen, YELLOW, [
    (50,100), 
    (100, 50), 
    (250, 50), 
    (300, 100)
])

pygame.draw.rect(screen, GREEN, pygame.Rect(100, 100, 150, 100))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
