import turtle
turtle.pensize(5)
for i in range(4):
    turtle.seth(90*i)
    turtle.fd(150)
    turtle.right(90)
    turtle.circle(-150,45)#右侧方向并按照原有方向旋转
    turtle.goto(0,0)#回到原点
turtle.done()

