# Нарисуйте «бабочку» из окружностей. Используйте функцию, рисующую окружность.

import turtle

turtle.shape()
turtle.hideturtle()

turtle.left(90)

def draw_circle(length):

    for i in range(40):
        angle = 360/40
        turtle.left(angle)
        turtle.forward(length)
    for i in range(40):
        angle = 360/40
        turtle.right(angle)
        turtle.forward(length)
    


for i in range(10):
    draw_circle(10 + i*2)

