# Нарисуйте пружину. Используйте функцию, рисующую дугу.

import turtle

turtle.shape()
turtle.hideturtle()
turtle.left(90)

def draw_arc(x, boоol):


    if boоol:
        for i in range(x):
            angle = 360/x/2
            turtle.right(angle)
            turtle.forward(10)
    else:
        for i in range(x):
            angle = 360/x/2
            turtle.left(angle)
            turtle.forward(10)


for i in range(5):
    
    draw_arc(20, True)

    draw_arc(5, True)


turtle.done()