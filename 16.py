import turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor('red')
pen = turtle.Turtle()
pen.speed(10)
pen.penup()
def draw_star(x,y,size):
    pen.goto(x,y)
    pen.pendown()
    pen.color('yellow')
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()
    pen.penup()
draw_star(-200,100,100)
def draw_small_star(x,y,size,angle):
    pen.goto(x,y)
    pen.setheading(angle)
    pen.pendown()
    pen.color('yellow')
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()
    pen.penup()
draw_small_star(-100,160,30,30)
draw_small_star(-60,120,30,0)
draw_small_star(-60,60,30,-30)
draw_small_star(-100,20,30,-60)
pen.hideturtle()
turtle.done()
turtle.mainloop()





















