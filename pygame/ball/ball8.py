import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

r = 40
x = screenX/2
y = r
vy = 0
a = 0.05

image = pygame.image.load("ball.png")
image = pygame.transform.scale(image, (2*r, 2*r))

def drawBall(x, y, r, color):
	screen.blit(image, pygame.Rect(x-r, y-r, 2*r, 2*r))

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
    drawBall(x, y, r, RED)
    pygame.display.flip()

    vy += a
    y += vy
    
    if y + r > screenY:        
        y = screenY - r
        vy = -0.9 * vy

    if y < r:
        y = r
        vy = 0