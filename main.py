import turtle
import random as rd

t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
t.width(2)


def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    rdc = (r, g, b)
    return rdc


for y in range(0, 360, 10):
    t.color(random_color())
    t.seth(y)
    t.circle(100)


