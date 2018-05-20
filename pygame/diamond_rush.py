import pygame, sys, math

WHITE = 255, 255, 255
YELLOW = 255, 255, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

pygame.font.init()
font = pygame.font.SysFont('Calibri', 24, bold=True)

img_size = 24
image = pygame.image.load("diamond.png")
image = pygame.transform.scale(image, (img_size, img_size))

rod = 40
angle = 0
score = 0
searching = True
reaching = returning = False

diamonds = [(80, 400), (240, 400), (400,400), (560, 400), (160,320), (320,320), (480, 320), (240, 240), (400,240), (320, 160)]

clock = pygame.time.Clock()

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            searching = False
            reaching = True

    phi = abs(angle%360 - 180)/180. * math.pi
    x = screenX/2 + rod * math.cos(phi)
    y = rod * math.sin(phi)
    
    if searching:
        angle += 1
        
    elif reaching:
        caught = False        
        for point in diamonds:
            xi, yi = point
            if abs(x-xi) + abs(y-yi) <= img_size/2:
                caught = True
                diamonds.remove(point)
                break
            
        rod += 5    
        if rod >= 500 or caught:
            reaching = False
            returning = True
          
    elif returning:
        rod -= 5
        if rod <= 40:
            if caught:
                score += 1
                
            rod = 40
            returning = False
            searching = True
            
    screen.fill(WHITE)
    
    for (xi, yi) in diamonds:
        screen.blit(image, pygame.Rect(xi - img_size/2, yi - img_size/2, img_size, img_size))

    pygame.draw.line(screen, YELLOW, (screenX/2, 0), (x, y), 3)
    
    if returning and caught:
        screen.blit(image, pygame.Rect(x - img_size/2, y - img_size/2, img_size, img_size))

    score_text = font.render("Score : " + str(score), False, YELLOW)
    screen.blit(score_text, (500, 30))

    pygame.display.flip()
