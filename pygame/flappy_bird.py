import sys, pygame, random

WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

x = 300
y = 200
sz = 40
a = 0.05
vy = 0

screenSize = screenX, screenY = 640, 480
screen = pygame.display.set_mode(screenSize)

pygame.font.init()
font = pygame.font.SysFont('Calibri', 40)

image = pygame.image.load("bird.jpg")
image = pygame.transform.scale(image, (sz, sz))

pipes = []
frameNo = 0
finished = False

clock = pygame.time.Clock()

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: 
            a = -0.2            

        if event.type == pygame.KEYUP: 
            a = 0.05        

    for pipe in pipes:
        check_rect = pygame.Rect(x+2, y+2, sz-4, sz-4)
        
        if check_rect.colliderect(pipe):
            text = font.render('Game Over!', False, RED)
            screen.blit(text, (280, 220))
            pygame.display.flip()
            finished = True
            break

    if not finished:
        screen.fill(WHITE)
        screen.blit(image, pygame.Rect(x, y, sz, sz))    

        for pipe in pipes:
            pygame.draw.rect(screen, GREEN, pipe)

        pygame.display.flip()

        vy += a
        y += vy

        if y + sz > screenY:
            y = screenY - sz
            vy = 0.0

        if y < 0:
            y = 0
            vy = 0.0

        for pipe in pipes:
            pipe.left -= 1                    

        frameNo += 1
        if frameNo % 150 == 0:
            height = random.randint(25, 250)
            lowerTop = height + random.randint(75, 250)
            pipes.append(pygame.Rect(screenX, 0, 10, height))
            pipes.append(pygame.Rect(screenX, lowerTop, 10, screenY-lowerTop))

        pipes = [pipe for pipe in pipes if pipe.left >= 0]
