import turtle

turtle.shape()

'''turtle.forward(50)
turtle.left(180-36)
turtle.forward(50)
turtle.left(180-36)
turtle.forward(50)
turtle.left(180-36)
turtle.forward(50)
turtle.left(180-36)
turtle.forward(50)
turtle.left(180-30)'''

def draw_star(n):
    angle = 180-180/n
    for i in range(n):
        turtle.forward(50)
        turtle.left(angle)
        

draw_star(11)

turtle.done()