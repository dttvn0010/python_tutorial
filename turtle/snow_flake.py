# http://python-with-science.readthedocs.io/en/latest/koch_fractal/koch_fractal.html#the-basic-unit
# Draw a Koch snowflake

from turtle import *

def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3., order-1)
            left(t)            
    else:
        forward(a)

color("sky blue")
size = 300
order = 5

penup()
backward(size/1.732)
left(30)
pendown()

tracer(100)
hideturtle()

for i in range(3):
    koch(size, order)
    right(120)

done()
