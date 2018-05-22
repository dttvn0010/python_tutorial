import pygame, sys, math

WHITE = 255, 255, 255
ORANGE = 255, 96, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

pygame.font.init()
font = pygame.font.SysFont('Calibri', 24, bold=True)

img_size = 24
image = pygame.image.load("diamond.png")
image = pygame.transform.scale(image, (img_size, img_size))

rod = rod_min = 40
rod_max = 500

angle = 0
score = 0

diamonds = [(80, 400), (240, 400), (400,400), (560, 400), (160,320), (320,320), (480, 320), (240, 240), (400,240), (320, 160)]

def draw_rod(x, y, phi, caught):
    pygame.draw.line(screen, ORANGE, (screenX/2, 0), (x, y), 3)
    
    cx = x + img_size/2 * math.cos(phi)
    cy = y + img_size/2 * math.sin(phi)

    rect = pygame.Rect(cx - img_size/2, cy - img_size/2, img_size, img_size)

    if caught:
        screen.blit(image, rect)

    pygame.draw.arc(screen, ORANGE, rect, math.pi/2 - phi, 3*math.pi/2 - phi, 3)

clock = pygame.time.Clock()
state = 'searching'

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if state == 'searching':
                state = 'reaching'

    phi = abs(angle%360 - 180) * math.pi/180
    x = screenX/2 + rod * math.cos(phi)
    y = rod * math.sin(phi)
    
    if state == 'searching':
        caught = False
        angle += 1
        
    elif state == 'reaching':        
        for point in diamonds:
            if abs(x - point[0]) + abs(y - point[1]) <= img_size/2:
                caught = True
                diamonds.remove(point)
                break
            
        rod += 5    
        if rod >= rod_max or caught:
            state = 'returning'
          
    elif state == 'returning':
        rod -= 5
        if rod <= rod_min:
            if caught:
                score += 1
                
            rod = rod_min
            state = 'searching'
            
    screen.fill(WHITE)
    
    for (xi, yi) in diamonds:
        screen.blit(image, pygame.Rect(xi - img_size/2, yi - img_size/2, img_size, img_size))
    
    draw_rod(x, y, phi, caught)

    score_text = font.render("Score : " + str(score), False, ORANGE)
    screen.blit(score_text, (500, 30))

    pygame.display.flip()