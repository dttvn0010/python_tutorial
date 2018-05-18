import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

sz = 80
x = (screenX-sz)/2
y = 0
vy = 0
a = 0.05

clock = pygame.time.Clock()
while True:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: 
            a = -0.1

        if event.type == pygame.KEYUP: 
            a = 0.05

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, pygame.Rect(x, y, sz, sz))
    pygame.display.flip()

    vy += a
    y += vy
    
    if y + sz > screenY:        
        y = screenY - sz
        vy = -0.9 * vy

    if y < 0:
        y = 0
        vy = 0