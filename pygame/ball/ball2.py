import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

sz = 80
x = (screenX-sz)/2
y = 0
vy = 1

clock = pygame.time.Clock()
while True:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, pygame.Rect(x, y, sz, sz))
    pygame.display.flip()

    y += vy
    
    if y + sz > screenY:
        vy = -1

    if y < 0:
        vy = 1