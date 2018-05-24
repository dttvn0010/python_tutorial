import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

ball_size = 80
x = (screenX - ball_size)/2
y = (screenY - ball_size)/2

clock = pygame.time.Clock()

while True:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, pygame.Rect(x, y, ball_size, ball_size))
    pygame.display.flip()