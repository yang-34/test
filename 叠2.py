import turtle
import math

def draw_hexagram(side_length):

    hexagram_height = side_length * math.sqrt(3)

    turtle.pencolor("black")

    turtle.penup()
    turtle.goto(-side_length / 2, 0)
    turtle.pendown()

    for _ in range(3):
        turtle.fd(side_length)
        turtle.seth(turtle.heading() + 120)

    turtle.penup()
    turtle.setheading(-60)
    turtle.goto(-side_length /4, hexagram_height * 1/4)
    turtle.pendown()

    for _ in range(3):
        turtle.fd(side_length /2)
        turtle.seth(turtle.heading() + 120)

draw_hexagram(side_length=200)

turtle.hideturtle()
turtle.done()