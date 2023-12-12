from turtle import *

def draw_square(side, x, y):
    up()
    setx(x)
    sety(y)
    down()
    begin_fill()
    color("blue")
    if x < 0:
        color("red")

    
    forward(side)
    right(90)
    forward(side)
    right(90)
    forward(side)
    right(90)
    forward(side)
    right(90)
    end_fill()
    # write a function that draws a draws
    # a square with either red or blue fill
    # depending on the starting x position
    # being positive (blue) or negative (red)
    
draw_square(40, -100, 100)
draw_square(60, 100, -100)
draw_square(100, -50, -20)
draw_square(80, 90, 30)
done()
