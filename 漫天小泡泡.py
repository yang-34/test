import turtle
import random

# 初始化设置
pen = turtle.Turtle()
pen.speed(0)  # 最快绘制速度
pen.width(2)   # 画笔粗细
screen = turtle.Screen()
screen.setup(800, 800)  # 设置画布大小
screen.bgcolor("white")  # 白色背景

# 定义泡泡颜色集合
colors = [
    "#FF69B4", "#00BFFF", "#7FFF00", "#FFD700",
    "#FF4500", "#DA70D6", "#00FA9A", "#FF6347",
    "#40E0D0"  
]

# 绘制随机泡泡
for _ in range(50):  # 绘制50个泡泡
    # 随机生成泡泡参数
    x = random.randint(-380, 380)
    y = random.randint(-380, 380)
    radius = random.randint(10, 40)
    
    # 设置泡泡属性
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    
    pen.color(random.choice(colors))
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

pen.hideturtle()
turtle.done()