from random import *
from turtle import *

colormode(255)
speed(0)
for i in range(20):
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    x = randint(-220,220)
    y = randint(-100,220)
    penup()
    goto(x,y)
    pendown()
    color(red, green, blue)
    begin_fill()
    circle(30)
    end_fill()
    right(90)
    forward(30)
    left(90)
done()