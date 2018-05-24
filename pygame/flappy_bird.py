import sys, pygame, random

screenSize = screenX, screenY = 640, 480
screen = pygame.display.set_mode(screenSize)

bird_size = 40
x = (screenX - bird_size)/2
y = (screenY - bird_size)/2
vy, a = 0, 0.05

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
    
    if not finished:
        screen.fill((255, 255, 255))        

        vy += a
        y += vy

        if y + bird_size > screenY:
            vy, y = 0, screenY - bird_size

        if y < 0:
            vy, y = 0, 0

        screen.blit(image, pygame.Rect(x, y, bird_size, bird_size))

        bird_rect = pygame.Rect(x+2, y+2, bird_size-4, bird_size-4)

        for pipe in pipes:
            pipe.left -= 1
            pygame.draw.rect(screen, (0, 255, 0), pipe)            

            if bird_rect.colliderect(pipe):
                text = font.render('Game Over!', False, (255, 0, 0))
                screen.blit(text, (280, 220))
                finished = True
                break

        pipes = [pipe for pipe in pipes if pipe.left >= 0]

        frameNo += 1
        if frameNo % 150 == 0:
            h1 = random.randint(25, 250)
            h2 = h1 + random.randint(75, 250)
            pipes.append(pygame.Rect(screenX, 0, 10, h1))
            pipes.append(pygame.Rect(screenX, h2, 10, screenY-h2))

        pygame.display.flip()