"""
Chương trình vẽ cây sử dụng hình học fractal
"""

#https://trinket.io/python/62ca928524

from turtle import *

def tree(branchLen):
    if branchLen > 5:
        forward(branchLen)
        right(20)
        tree(branchLen-15)
        left(40)
        tree(branchLen-15)
        right(20)
        backward(branchLen)

left(90)
up()
backward(100)
down()
color("green")
tree(75)

done()
