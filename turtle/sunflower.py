# Sunflower with a phyllotactic pattern
# By Deborah R. Fowler
# Modified from 
# http://www.deborahrfowler.com/PythonResources/PythonTurtle.html

import math
from turtle import *

shape("turtle")
color("black")
speed(0)

def drawSunflower(numseeds, numpetals, angle, cspread):
    fillcolor("orange")
    phi = angle * (math.pi / 180.0)
   
    for i in range (numseeds + numpetals):
      # figure out the next x, y position
      r = cspread * math.sqrt(i)
      theta = i * phi
      x = r * math.cos(theta)
      y = r * math.sin(theta)

      # move the turtle and orient it correctly
      penup()
      goto(x, y)
      setheading(i * angle)
      pendown()

      if i <  numseeds:
        stamp()
      else:
        drawPetal()
          
def drawPetal():
    fillcolor("yellow")
    begin_fill()
    right(20)
    forward(70)
    left(40)
    forward(70)
    left(140)
    forward(70)
    left(40)
    forward(70)
    end_fill()

drawSunflower(160, 40, 137.508, 4)

hideturtle()
done()
