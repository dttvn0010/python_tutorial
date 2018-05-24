import pygame, sys, math

WHITE = 255, 255, 255
ORANGE = 255, 96, 0

screenX, screenY = 640, 480
screen = pygame.display.set_mode((screenX, screenY))

rect_size = 24
rod = rod_min = 40
rod_max = 500

pygame.font.init()
font = pygame.font.SysFont('Calibri', 28)

image = pygame.image.load("diamond.png")
image = pygame.transform.scale(image, (rect_size, rect_size))

diamonds = [(80, 400), (240, 400), (400,400), (560, 400), (160,320), (320,320), (480, 320), (240, 240), (400,240), (320, 160)]
score = 0
angle = 0
clock = pygame.time.Clock()

def draw_rod(x, y, phi):
    pygame.draw.line(screen, ORANGE, (screenX/2, 0), (x, y), 3)
    
    cx = x + rect_size/2 * math.cos(phi)
    cy = y + rect_size/2 * math.sin(phi)

    rect = pygame.Rect(cx - rect_size/2, cy - rect_size/2, rect_size, rect_size)

    pygame.draw.arc(screen, ORANGE, rect, math.pi/2 - phi, 3*math.pi/2 - phi, 3)

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    phi = abs(angle%360 - 180) * math.pi/180
    x = screenX/2 + rod * math.cos(phi)
    y = rod * math.sin(phi)
    
    angle += 1
            
    screen.fill(WHITE)    
    
    draw_rod(x, y, phi)

    for (xi, yi) in diamonds:
        screen.blit(image, pygame.Rect(xi - rect_size/2, yi - rect_size/2, rect_size, rect_size))

    score_text = font.render("Score : " + str(score), False, ORANGE)
    screen.blit(score_text, (500, 30))

    pygame.display.flip()
