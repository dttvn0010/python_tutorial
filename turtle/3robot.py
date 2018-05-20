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

t1 = createTurtle(-100, 0)
t2 = createTurtle(0, 173)
t3 = createTurtle(100, 0)

while distance(t1, t2) > 4:
    alpha1 = t1.towards(t2.pos())
    t1.setheading(alpha1)

    alpha2 = t2.towards(t3.pos())
    t2.setheading(alpha2)

    alpha3 = t3.towards(t1.pos())
    t3.setheading(alpha3)

    t1.forward(2)
    t2.forward(2)
    t3.forward(2)    

turtle.done()
