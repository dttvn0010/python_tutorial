import pygame, sys
import math

WHITE = 255, 255, 255

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))
screen.fill(WHITE)

ball_size = 80
x = (screenX - ball_size)/2
y = (screenY - ball_size)/2

image = pygame.image.load('ball.png')
image = pygame.transform.scale(image, (ball_size, ball_size))
screen.blit(image, pygame.Rect(x, y, ball_size, ball_size))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
