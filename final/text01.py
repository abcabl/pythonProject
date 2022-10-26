import turtle as t
import math

t.hideturtle()#隐藏一下小海龟
t.speed(7)  #设置画笔速度

#开始画盾牌大体
t.color('red','red')
t.up()
t.goto(0,-180)
t.down()
t.begin_fill()
t.circle(180)
t.end_fill()#最大的⚪

t.color('white','white')
t.up()
t.goto(0,-145)
t.down()
t.begin_fill()
t.circle(145)
t.end_fill()

t.color('red','red')
t.up()
t.goto(0,-110)
t.down()
t.begin_fill()
t.circle(110)
t.end_fill()

t.color('blue','blue')
t.up()
t.goto(0,-75)
t.down()
t.begin_fill()
t.circle(75)
t.end_fill()#最小的一个⚪

#画五角星
pi=3.1415926
a=math.sin(0.4*pi)
a=a*75*2 #计算需要前进的距离
t.up()
t.goto(0,75)
t.seth(-72)#调整角度
t.color('white','white')
t.down()
t.begin_fill()
t.forward(a)
for i in range(5):    #这里连着5笔都是重复的步骤，可以使用一个for循环
    t.right(144)
    t.forward(a)
t.end_fill()

t.done()

