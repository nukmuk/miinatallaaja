from turtle import *


def draw_circle(x, y, radius):
    up()
    setx(x)
    sety(y - radius)
    down()
    circle(radius)
    up()


draw_circle(50, 50, 30)
draw_circle(-50, 50, 30)
draw_circle(0, 0, 60)
up()
setx(0)
sety(0)
done()
