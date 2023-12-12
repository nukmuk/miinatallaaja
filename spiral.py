from turtle import *


def draw_spiral(colorr, arcs, radius, growth, weight=1):
    color(colorr)
    pensize(weight)
    for i in range(arcs):
        circle(radius, 90)
        radius += growth


draw_spiral("black", 20, 10, 3)
draw_spiral("red", 10, 20, 4, 3)
draw_spiral("blue", 10, -20, -4, 3)
done()
