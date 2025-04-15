import turtle

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

side_length = 200

for _ in range(3):
    turtle.fd(side_length)
    turtle.seth(turtle.heading() + 120)

turtle.hideturtle()
turtle.done()