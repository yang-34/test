import turtle
import random

# 初始化设置
pen = turtle.Turtle()
pen.speed(0)
pen.width(3)
turtle.bgcolor("black")  # 设置黑色背景

# 定义星星颜色集合
colors = [
    "#FF0000", "#00FF00", "#0000FF", "#FFA500",  # 红、绿、蓝、橙
    "#FF69B4", "#00BFFF", "#FFD700", "#9400D3"   # 粉、天蓝、金、紫
]

# 绘制随机星星
for _ in range(50):
    # 生成随机参数
    x = random.randint(-380, 380)
    y = random.randint(-380, 380)
    # 修改星星大小为固定值
    size = 10  # 统一设置为10像素
    
    # 设置画笔属性
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    
    # 绘制五角星（保持现有逻辑）
    pen.color(random.choice(colors))
    pen.begin_fill()  # 开始填充
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()    # 结束填充

pen.hideturtle()
turtle.done()