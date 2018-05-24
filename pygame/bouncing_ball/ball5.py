import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

ball_size = 80
x = (screenX - ball_size)/2
y = 0
vy = 0
a = 0.05

image = pygame.image.load("ball.png")
image = pygame.transform.scale(image, (ball_size, ball_size))

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
    screen.blit(image, pygame.Rect(x, y, ball_size, ball_size))
    pygame.display.flip()

    vy += a
    y += vy
    
    if y + ball_size > screenY:
        y = screenY - ball_size
        vy = -0.9 * vy

    if y < 0:
        y = 0
        vy = 0
