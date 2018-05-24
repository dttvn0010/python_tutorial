import pygame, time, sys

WHITE = 255, 255, 255
GREEN = 0, 255, 0

ndisks = 4
screenX, screenY = 640, 480

column_width = screenX/3
disk_height = screenY/ndisks

disks = [[], [], []]

screen = pygame.display.set_mode((screenX, screenY))

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

for i in range(ndisks):
    disk = {'width' : column_width * (ndisks - i) / ndisks}
    pushDisk(disk, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(WHITE)

    for i in range(3):
        for disk in disks[i]:
            pygame.draw.rect(screen, GREEN, getRect(disk))

    pygame.display.flip()

    time.sleep(0.01)