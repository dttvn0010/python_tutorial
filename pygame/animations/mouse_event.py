import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

radius = 40
x, y = screenX/2, screenY/2

moving = False
clock = pygame.time.Clock()

while True:
    clock.tick(100)

    screen.fill(WHITE)	
    pygame.draw.circle(screen, RED, (int(x), int(y)), radius)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()            
            dx = mouse_x - x
            dy = mouse_y - y

            if dx*dx + dy*dy < radius*radius:
                moving = True

        if event.type == pygame.MOUSEMOTION and moving:
            x, y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            moving = False
