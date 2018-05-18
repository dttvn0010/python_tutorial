import turtle

def draw_square(size, color):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

turtle.left(20)
draw_square(200, 'red')

turtle.left(30)
draw_square(200, 'green')

turtle.left(40)
draw_square(200, 'blue')

turtle.done()