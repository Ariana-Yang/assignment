import turtle

# 设置窗口大小和背景颜色
turtle.setup(600, 600)
turtle.bgcolor("white")

# 创建一个画笔
pen = turtle.Turtle()
pen.speed(10)

# 画盾牌的外形（简单矩形代表）
def draw_shield():
    pen.penup()
    pen.goto(-100, 200)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("green")  # 设置填充颜色
    for _ in range(2):
        pen.forward(200)
        pen.right(90)
        pen.forward(300)
        pen.right(90)
    pen.end_fill()

# 画中间书的简化图案
def draw_book():
    pen.penup()
    pen.goto(-60, 50)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("yellow")
    for _ in range(2):
        pen.forward(120)
        pen.right(90)
        pen.forward(60)
        pen.right(90)
    pen.end_fill()

    # 画书页线条
    pen.penup()
    pen.goto(-60, 20)
    pen.pendown()
    pen.forward(120)
    pen.penup()
    pen.goto(-60, 0)
    pen.pendown()
    pen.forward(120)

# 画一条简单的横线，作为纹章的代表
def draw_cross():
    pen.penup()
    pen.goto(-100, 100)
    pen.pendown()
    pen.color("red")
    pen.width(10)
    pen.forward(200)

# 主函数，调用各部分绘制
def draw_logo():
    draw_shield()
    draw_book()
    draw_cross()

# 调用绘制徽标函数
draw_logo()

# 隐藏画笔，完成绘图
pen.hideturtle()

# 结束程序
turtle.done()
