import turtle


def draw_equilateral_triangle(size):
    """绘制一个等边三角形"""
    for _ in range(3):
        turtle.fd(size)
        turtle.left(120)


def draw_pin_shape():
    """绘制品字形的三个等边三角形"""
    size = 100  # 三角形边长

    # 绘制上方三角形
    turtle.penup()
    turtle.goto(0, size * (3 ** 0.5) / 2)  # 计算上方顶点位置
    turtle.pendown()
    turtle.seth(0)  # 设置方向向右
    draw_equilateral_triangle(size)

    # 绘制左下方三角形
    turtle.penup()
    turtle.goto(-size / 2, 0)  # 左下方顶点位置
    turtle.pendown()
    turtle.seth(0)
    draw_equilateral_triangle(size)

    # 绘制右下方三角形
    turtle.penup()
    turtle.goto(size / 2, 0)  # 右下方顶点位置
    turtle.pendown()
    turtle.seth(0)
    draw_equilateral_triangle(size)


# 设置画布
turtle.speed(5)  # 中等绘制速度
turtle.title("叠加等边三角形的绘制")
turtle.bgcolor("white")
turtle.color("black")

# 绘制品字形
draw_pin_shape()

# 完成绘制
turtle.hideturtle()
turtle.done()
