import sys, pygame, random

screenSize = screenX, screenY = 640, 480
screen = pygame.display.set_mode(screenSize)

bird_size = 40
x = (screenX - bird_size)/2
y = (screenY - bird_size)/2
a = 0.05
vy = 0

pygame.font.init()
font = pygame.font.SysFont('Calibri', 40)

image = pygame.image.load("bird.jpg")
image = pygame.transform.scale(image, (bird_size, bird_size))

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

    check_rect = pygame.Rect(x+2, y+2, bird_size-4, bird_size-4)

    for pipe in pipes:
        if check_rect.colliderect(pipe):
            text = font.render('Game Over!', False, (255, 0, 0))
            screen.blit(text, (280, 220))
            pygame.display.flip()
            finished = True
            break

    if not finished:
        screen.fill((255, 255, 255))
        screen.blit(image, pygame.Rect(x, y, bird_size, bird_size))

        for pipe in pipes:
            pygame.draw.rect(screen, (0, 255, 0), pipe)

        pygame.display.flip()

        vy += a
        y += vy

        if y + bird_size > screenY:
            y = screenY - bird_size
            vy = 0.0

        if y < 0:
            y = 0
            vy = 0.0

        for pipe in pipes:
            pipe.left -= 1

        pipes = [pipe for pipe in pipes if pipe.left >= 0]

        frameNo += 1
        if frameNo % 150 == 0:
            height = random.randint(25, 250)
            lowerTop = height + random.randint(75, 250)
            pipes.append(pygame.Rect(screenX, 0, 10, height))
            pipes.append(pygame.Rect(screenX, lowerTop, 10, screenY-lowerTop))
