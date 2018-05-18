import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

def drawBall(x, y, r, color):
    pygame.draw.ellipse(screen, color, pygame.Rect(x-r, y-r, 2*r, 2*r))

r = 40
x = screenX/2
y = r
vy = 1

clock = pygame.time.Clock()
while True:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(WHITE)
    drawBall(x, y, r, RED)
    pygame.display.flip()

    y += vy
    
    if y + r > screenY:
        vy = -1

    if y < r:
        vy = 1