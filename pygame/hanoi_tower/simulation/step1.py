#Animated Tower of Hanoi Graphical display of the moves to solve Tower of Hanoi. Authour: Alan Richmond, Python3.Codes
import pygame, time, sys

WHITE = 255, 255, 255
GREEN = 0, 255, 0

N = 4
screenX, screenY = 640, 480

column_width = screenX/3
disk_height = screenY/N

disks = [[], [], []]

screen = pygame.display.set_mode((screenX, screenY))
screen.fill(WHITE)

def pushDisk(disk, column):
    disk['column'] = column
    disk['level'] = len(disks[column]) + 1
    disks[column].append(disk)

def popDisk(column):
    disks[column].pop()

def getRect(disk):
    xcenter = (disk['column'] + 0.5) * column_width
    left = xcenter - disk['width']/2
    top = screenY - disk_height * disk['level']
    return pygame.Rect(left, top, disk['width'], disk_height-1)

for i in range(N):
    disk = {'width' : column_width * (N - i) / N}
    pushDisk(disk, 0)
    pygame.draw.rect(screen, GREEN, getRect(disk))

pygame.display.flip()
time.sleep(3)
