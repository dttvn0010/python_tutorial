import pygame, sys

WHITE = 255, 255, 255
RED = 255, 0, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

radius = 40
x, y = screenX/2, screenY/2
vx, vy = 0, 0

clock = pygame.time.Clock()

while True:
    clock.tick(100)
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_UP:
                vy = -1
				
            if event.key == pygame.K_DOWN:
                vy = 1
				
            if event.key == pygame.K_LEFT:
                vx = -1
				
            if event.key == pygame.K_RIGHT:
                vx = 1
            
        if event.type == pygame.KEYUP:
            vx, vy = 0, 0

    x += vx
    y += vy
	
    x = min(max(x, radius), screenX-radius)
    y = min(max(y, radius), screenY-radius)
	
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(x), int(y)), radius)
    pygame.display.flip()
