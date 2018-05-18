# Sunflower with a phyllotactic pattern
# By Deborah R. Fowler
# Modified from 
# http://www.deborahrfowler.com/PythonResources/PythonTurtle.html

import math
import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.color("black")
tina.speed(0)

def drawSunflower(t, numseeds, numpetals, angle, cspread):
    t.fillcolor("orange")
    phi = angle * (math.pi / 180.0)
   
    for i in range (numseeds + numpetals):
      # figure out the next x, y position
      r = cspread * math.sqrt(i)
      theta = i * phi
      x = r * math.cos(theta)
      y = r * math.sin(theta)

      # move the turtle and orient it correctly
      t.penup()
      t.goto(x, y)
      t.setheading(i * angle)
      t.pendown()

      if i <  numseeds:
        t.stamp()
      else:
        drawPetal(t)
          
def drawPetal(t):
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(20)
    t.forward(70)
    t.left(40)
    t.forward(70)
    t.left(140)
    t.forward(70)
    t.left(40)
    t.forward(70)
    t.end_fill()

drawSunflower(tina, 160, 40, 137.508, 4)

tina.hideturtle()
turtle.done()