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

def pushDisk(disk, column):
    disk.column = column
    disk.level = len(disks[column]) + 1
    disk.calcRect()
    disks[column].append(disk)

def popDisk(column):
    disks[column].pop()

class Disk():
    def __init__(self, width):
        self.width = width
        self.column = 0
        self.level = 0    

    def calcRect(self):
        xcenter = (self.column + 0.5) * column_width
        left = xcenter - self.width/2
        top = screenY - disk_height * self.level
        self.rect = pygame.Rect(left, top, self.width, disk_height-1)

    def animateMove(self, old_rect, new_rect):
        pygame.draw.rect(screen, WHITE, old_rect)
        pygame.draw.rect(screen, GREEN, new_rect)
        pygame.display.flip()
        time.sleep(0.5)

    def moveToColumn(self, column):        
        popDisk(self.column)
        
        rect1 = self.rect
        rect2 = pygame.Rect(rect1)
        rect2.top = 0        

        pushDisk(self, column)
        rect3 = pygame.Rect(self.rect)
        rect3.top = 0

        self.animateMove(rect1, rect2)
        self.animateMove(rect2, rect3)
        self.animateMove(rect3, self.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

def moveDisk(src, dest, ndisks):
    if ndisks > 0:
        moveDisk(src, 3-src-dest, ndisks-1)
        disks[src][-1].moveToColumn(dest)
        moveDisk(3-src-dest, dest, ndisks-1)

for i in range(ndisks):
    disk_width = column_width * (ndisks - i) / ndisks
    disk = Disk(disk_width)
    pushDisk(disk, 0)
    pygame.draw.rect(screen, GREEN, disk.rect)

pygame.display.flip()
moveDisk(0, 2, ndisks)
