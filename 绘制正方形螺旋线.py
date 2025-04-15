import turtle


def draw_square_spiral_up_left(side_length, increment, turns):

    turtle.pencolor("black")
    turtle.speed(0)

    turtle.setheading(90)

    for _ in range(turns):
        turtle.forward(side_length)
        turtle.left(90)
        side_length += increment

draw_square_spiral_up_left(side_length=3, increment=3, turns=99)

turtle.hideturtle()
turtle.done()