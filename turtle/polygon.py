"""
Chương trình vẽ đa giác đều
"""

from turtle import *

num_sides = 8
side_length = 50
angle = 360.0 / num_sides 

for i in range(num_sides):
    forward(side_length)
    right(angle)
    
done()
