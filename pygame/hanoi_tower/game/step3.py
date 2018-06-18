import pygame, time, sys

WHITE = 255, 255, 255
GREEN = 0, 255, 0

N = 4
screenX, screenY = 640, 480

column_width = screenX/3
disk_height = screenY/N

disks = [[], [], []]

screen = pygame.display.set_mode((screenX, screenY))

pygame.font.init()
font = pygame.font.SysFont('Calibri', 36, bold=True)

def getRect(disk):
    xcenter = (disk['column'] + 0.5) * column_width
    left = xcenter - disk['width']/2
    top = screenY - disk_height * disk['level']
    return pygame.Rect(left, top, disk['width'], disk_height-1)

def canPush(disk, column):    
    if len(disks[column]) == 0:
        return True

    top_disk = disks[column][-1]
    return top_disk['width'] > disk['width']

def pushDisk(disk, column):
    disk['column'] = column
    disk['level'] = len(disks[column]) + 1
    disks[column].append(disk)

def popDisk(column):
    disks[column].pop()

for i in range(N):
    disk = {'width' : column_width * (N - i) / N}
    pushDisk(disk, 0)

move_disk = None

while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(3):
                if len(disks[i]) == 0 :
                    continue

                top_disk = disks[i][-1]
                top_disk_rect = getRect(top_disk)
                
                if top_disk_rect.collidepoint(mouse_pos):
                    move_disk = top_disk
                    move_rect = top_disk_rect
                    break 

        if event.type == pygame.MOUSEMOTION and move_disk != None:
            move_rect.topleft = mouse_pos            

        if event.type == pygame.MOUSEBUTTONUP and move_disk != None:
            column = int(mouse_pos[0]/column_width)

            if canPush(move_disk, column):
                popDisk(move_disk['column'])
                pushDisk(move_disk, column)

            move_disk = None

    screen.fill(WHITE)

    for i in range(3):
        for disk in disks[i]:
            if disk != move_disk:
                pygame.draw.rect(screen, GREEN, getRect(disk))

    if move_disk != None:
        pygame.draw.rect(screen, GREEN, move_rect)

    if len(disks[2]) == N:
        text = font.render('Well done!', False, (255, 0, 0))
        screen.blit(text, (280, 200))        

    pygame.display.flip()

    time.sleep(0.01)
