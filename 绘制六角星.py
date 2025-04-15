import turtle
import math

def draw_hexagram(side_length):
    hexagram_height = side_length * math.sqrt(3) * 2/3
    turtle.pencolor("black")

    turtle.penup()
    turtle.seth(30)
    turtle.goto(-hexagram_height / 2, 0)
    turtle.pendown()

    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)

    turtle.penup()
    turtle.seth(-150)
    turtle.goto(hexagram_height / 2, 0)
    turtle.pendown()

    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)

draw_hexagram(side_length=180)

turtle.hideturtle()
turtle.done()