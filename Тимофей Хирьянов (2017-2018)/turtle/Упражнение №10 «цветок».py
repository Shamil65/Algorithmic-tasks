import turtle
import math


turtle.shape()
turtle.hideturtle()


def drawing_a_circle(number_of_sides, R, turn=True):
    angle = 360/number_of_sides
    length_of_the_triangle = 2 * R * math.sin(math.pi / number_of_sides)

    turtle.left(angle)
    turtle.forward(length_of_the_triangle)

    for i in range(number_of_sides-1):
        if turn == True:
            turtle.left(angle)
            turtle.forward(length_of_the_triangle)
        else:
            turtle.right(angle)
            turtle.forward(length_of_the_triangle)


for i in range(20):
    drawing_a_circle(20, 50, turn=False)
    drawing_a_circle(20, 50, turn=True)



