
import turtle
import math

number_of_sides = 3
R = 45

def draww(number_of_sides, length_of_the_triangle):
    angle = 360/number_of_sides

    for i in range(number_of_sides):
        
        turtle.left(angle)
        turtle.forward(length_of_the_triangle)


for i in range(10):
    length_of_the_triangle = 2 * R * math.sin(math.pi / number_of_sides)
    x = (180-360/number_of_sides)/2
    turtle.left(x)

    draww(number_of_sides, length_of_the_triangle)
    turtle.right(x)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

    number_of_sides += 1
    R += 10
