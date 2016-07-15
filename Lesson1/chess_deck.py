import turtle
turtle.speed('fast')
side=40
y = 0
x = 0
for k in range(8):

    if k % 2 == 0:
        x = 0
    else:
        x = side
    turtle.goto(x,y)
    for i in range(4):
        turtle.begin_fill()

        for l in range(4) :
            turtle.forward(side)
            turtle.left(90)

        turtle.end_fill()
        turtle.penup()
        turtle.forward(side)
        turtle.forward(side)

    y += side

turtle.goto(0,0)
turtle.pendown()
for q in range(4) :
    turtle.forward(320)
    turtle.left(90)


turtle.exitonclick()
