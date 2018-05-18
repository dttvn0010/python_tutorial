class Rook:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveX(self, new_x):
    	self.x = new_x

    def moveY(self, new_y):
    	self.y = new_y

rook1 = Rook(0, 0)
rook2 = Rook(7, 0)

rook1.moveX(4)
print('rook1 at ',  (rook1.x, rook1.y))

rook2.moveY(5)
print('rook2 at ', (rook2.x, rook2.y))
