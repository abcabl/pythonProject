import turtle as t

t.speed(0)


def drawCircle():#画⚪函数
    t.pendown()
    t.circle(20)  # 半径为20
    t.penup()
    t.fd(40)


def drawRowCircle(n):
    for i in range(n, 1, -1):  # 从第一排往下画圆 5432
        for j in range(i):  # 根据i的变化画i个圆
            drawCircle()
        t.fd(-i * 40 - 20)  # 往左走，回到这一排的第一个圆的位置
        # 这里减20是因为循环一次（画了一排圆之后）圆心停在半径20处
        # 即此排中第一个圆到最后一个圆的总共长度是i个40+20,小海龟在最后一个圆的起点处
        t.right(90)  # 小海龟向右转90°
        t.fd(40)  # 向下走一个直径的距离
        t.left(90)  # 箭头向下向左即向右
        t.fd(40)
    drawCircle()


drawRowCircle(5)
t.hideturtle()
t.done()


