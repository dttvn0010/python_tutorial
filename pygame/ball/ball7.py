import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

def drawBall(x, y, r, color):
    pygame.draw.ellipse(screen, color, pygame.Rect(x-r, y-r, 2*r, 2*r))

r = 40
x = screenX/2
y = screenY/2
moving = False
clock = pygame.time.Clock()

while True:
    clock.tick(100)

    screen.fill(WHITE)
    drawBall(x, y, r, RED)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = x - mouse_x
            dy = y - mouse_y

            if dx*dx + dy*dy < r*r:
                moving = True

        if event.type == pygame.MOUSEMOTION and moving:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x = mouse_x
            y = mouse_y

        if event.type == pygame.MOUSEBUTTONUP:
            moving = False