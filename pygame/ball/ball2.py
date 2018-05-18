import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))
r = 40

def drawBall(x, y, r, color):
    pygame.draw.ellipse(screen, color, pygame.Rect(x-r, y-r, 2*r, 2*r))

screen.fill(WHITE)
drawBall(screenX/2, screenY/2, r, RED)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()