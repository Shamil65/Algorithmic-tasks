import turtle
import math

turtle.shape()
turtle.speed(0)
turtle.hideturtle()

def draw_circle(x, color_='black', fill=False, left_=True, lenth_=5):
    
    L = int((2 * math.pi * x / 2 / lenth_) // 1)
    print(L, 2 * math.pi * x / 2)
    angle = 360 / L

    if fill:
        turtle.begin_fill()
    
    for i in range(L):

        turtle.color(color_)
        if left_:
            turtle.left(angle)
        else:
            turtle.right(angle)
        turtle.forward(lenth_)

    if fill:
        turtle.end_fill()
        

def draw_arc(x, color_='black', lenth_=5):
    
    L = int((2 * math.pi * x / 2 / lenth_) // 1)
    print(L, 2 * math.pi * x / 2)
    angle = 360 / L
    
    for i in range(L//2):

        turtle.color(color_)
        turtle.left(angle)
        turtle.forward(lenth_)

draw_circle(100, color_='yellow', fill=True)

turtle.penup()
turtle.goto(-25, 75)
turtle.pendown()

draw_circle(20, color_='blue', fill=True, left_=False)

turtle.penup()
turtle.goto(25, 75)
turtle.pendown()

draw_circle(20, color_='blue', fill=True, left_=False)

turtle.penup()
turtle.goto(-20, 50)
turtle.pendown()

turtle.color('red')
turtle.width(5)
turtle.right(90)
draw_arc(40)

turtle.done()