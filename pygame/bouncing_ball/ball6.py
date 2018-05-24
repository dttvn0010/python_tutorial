import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

ball_size = 80
x = (screenX - ball_size)/2
y = (screenY - ball_size)/2

image = pygame.image.load("ball.png")
image = pygame.transform.scale(image, (ball_size, ball_size))

moving = False
clock = pygame.time.Clock()

while True:
    clock.tick(100)

    screen.fill(WHITE)
    screen.blit(image, pygame.Rect(x, y, ball_size, ball_size))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            r = ball_size/2
            dx = x + r - mouse_x
            dy = y + r - mouse_y

            if dx*dx + dy*dy < r*r:
                moving = True

        if event.type == pygame.MOUSEMOTION and moving:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x = mouse_x - ball_size/2
            y = mouse_y - ball_size/2

        if event.type == pygame.MOUSEBUTTONUP:
            moving = False