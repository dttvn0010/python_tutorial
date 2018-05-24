#Animated Tower of Hanoi Graphical display of the moves to solve Tower of Hanoi. Authour: Alan Richmond, Python3.Codes
import pygame, time, sys

WHITE = 255, 255, 255
GREEN = 0, 255, 0

ndisks = 4
screenX, screenY = 640, 480

column_width = screenX/3
disk_height = screenY/ndisks

disks = [[], [], []]

screen = pygame.display.set_mode((screenX, screenY))
screen.fill(WHITE)

def getRect(disk):
    xcenter = (disk['column'] + 0.5) * column_width
    left = xcenter - disk['width']/2
    top = screenY - disk_height * disk['level']
    return pygame.Rect(left, top, disk['width'], disk_height-1)

def pushDisk(disk, column):
    disk['column'] = column
    disk['level'] = len(disks[column]) + 1
    disks[column].append(disk)

def popDisk(column):
    disks[column].pop()

def animateMove(old_rect, new_rect):
    pygame.draw.rect(screen, WHITE, old_rect)
    pygame.draw.rect(screen, GREEN, new_rect)
    pygame.display.flip()
    time.sleep(0.5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

def moveDisk(disk, column):        
    popDisk(disk['column'])
    
    rect1 = getRect(disk)
    rect2 = pygame.Rect(rect1)
    rect2.top = 0

    pushDisk(disk, column)
    rect4 = getRect(disk)
    rect3 = pygame.Rect(rect4)
    rect3.top = 0

    animateMove(rect1, rect2)
    animateMove(rect2, rect3)
    animateMove(rect3, rect4)

def hanoi(src, dest, ndisks):
    if ndisks > 0:
        hanoi(src, 3-src-dest, ndisks-1)
        moveDisk(disks[src][-1], dest)
        hanoi(3-src-dest, dest, ndisks-1)

for i in range(ndisks):
    disk = {'width' : column_width * (ndisks - i) / ndisks}
    pushDisk(disk, 0)
    pygame.draw.rect(screen, GREEN, getRect(disk))

pygame.display.flip()
hanoi(0, 2, ndisks)