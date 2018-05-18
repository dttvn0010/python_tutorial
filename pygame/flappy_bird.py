import sys, pygame, random

WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

screenSize = screenX, screenY = 640, 480
screen = pygame.display.set_mode(screenSize)

pygame.font.init()
font = pygame.font.SysFont('Calibri', 40)

class Bird():
    def __init__(self, rect, a):        
        self.rect = rect
        self.vy = 0.0
        self.a = a
        image = pygame.image.load("bird.jpg")
        self.image = pygame.transform.scale(image, rect.size)

    def move(self):        
        self.vy += self.a        
        self.rect.top += self.vy

        if self.rect.bottom > screenY:
            self.rect.bottom = screenY
            self.vy = 0.0

        if self.rect.top < 0:
            self.rect.top = 0
            self.vy = 0.0

    def crashWith(self, pipes):
        for pipe in pipes:
            if self.rect.colliderect(pipe):
                return True                
        return False

def drawBird(bird):
    screen.blit(bird.image, bird.rect)    

bird = Bird(pygame.Rect(300, 200, 40, 40), 0.05)
pipes = []

clock = pygame.time.Clock()
frameNo = 0
finished = False

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: 
            bird.a = -0.2            

        if event.type == pygame.KEYUP: 
            bird.a = 0.05
    
    if bird.crashWith(pipes):
        text = font.render('Game Over!', False, RED)
        screen.blit(text, (280, 220))
        pygame.display.flip()
        finished = True

    if not finished:
        screen.fill(WHITE)

        bird.move()
        drawBird(bird)

        for pipe in pipes:
            pipe.left -= 1
            pygame.draw.rect(screen, GREEN, pipe)            

        pygame.display.flip()

        frameNo += 1
        if frameNo % 150 == 0:
            height = random.randint(25, 250)
            lowerTop = height + random.randint(75, 250)
            pipes.append(pygame.Rect(screenX, 0, 10, height))
            pipes.append(pygame.Rect(screenX, lowerTop, 10, screenX-lowerTop))

        pipes = [pipe for pipe in pipes if pipe.left >= 0]
