import turtle

# 初始化turtle
pen = turtle.Turtle()
pen.speed(0)  # 最快绘制速度
screen = turtle.Screen()
screen.bgcolor("white")

# 定义10种环的颜色（可根据需要修改）
colors = [
    "#FF0000", "#FF7F00", "#FFFF00", "#00FF00",
    "#00FFFF", "#0000FF", "#4B0082", "#9400D3",
    "#FF1493", "#FFD700"
]

# 绘制同心圆
for i in range(10):
    radius = 20 * (i + 1)  # 半径从20开始，每次增加20
    pen.penup()
    pen.goto(0, -radius)   # 移动到圆心下方起始位置
    pen.pendown()
    
    pen.color(colors[i % len(colors)])  # 设置画笔颜色
    pen.circle(radius)     # 直接绘制圆形轮廓

pen.hideturtle()
turtle.done()