"""
Chương trình vẽ bông hoa
"""

# http://nghiaho.com/?p=1603
# Thanks goes to Raphael for improving the original slow clunky code

from turtle import *

def petal(radius,steps):
    circle(radius,90,steps)
    left(90)
    circle(radius,90,steps)

num_petals = 8
steps = 8
radius = 100

speed(0)

for i in range(num_petals):
    setheading(0)
    right(360*i/num_petals)
    petal(radius,steps)

done()
