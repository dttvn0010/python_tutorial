import sys, pygame

WHITE = 255, 255, 255
screenSize = screenX, screenY = 640, 480
screen = pygame.display.set_mode(screenSize)

bird_size = 40
image = pygame.image.load("bird.jpg")
image = pygame.transform.scale(image, (bird_size, bird_size))

x = (screenX - bird_size)/2
y = (screenY - bird_size)/2

clock = pygame.time.Clock()

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(WHITE)
    screen.blit(image, pygame.Rect(x, y, bird_size, bird_size))
    pygame.display.flip()
