"""
Chương trình vẽ chuyển động của tên lửa đuổi theo máy bay
 + Tên lửa trên mặt đất ở tọa độ (0,0)
 + Máy bay ở tọa độ (100, 100) và chuyển động theo phương ngang
 + Tên lửa đuổi theo máy bay, vận tốc tên lửa gấp 2 vận tốc máy bay 
 + Tên lửa luôn hướng về phía máy bay trong quá trình chuyển động

Vẽ quỹ đạo chuyển động của máy bay và tên lửa
"""

import turtle

def createTurtle(x,y):
  t = turtle.Turtle()
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.speed(0)
  return t

def distance(t1, t2):
  x1, y1 = t1.pos()
  x2, y2 = t2.pos()
  return abs(x2-x1) + abs(y2-y1)

airplane = createTurtle(100, 100)
missile = createTurtle(0, 0)

while distance(airplane, missile) > 2:
    alpha = missile.towards(airplane.pos())
    missile.setheading(alpha)
    
    airplane.forward(1)
    missile.forward(2)

turtle.done()
