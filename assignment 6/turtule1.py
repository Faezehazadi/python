import turtle

p = turtle.Pen()
turtle.bgcolor("steelblue4")
p.pencolor("white")
x_cord =0

for i in range(3,8):
    for j in range (i):
        degree = 360 / i
        p.left(degree)
        p.forward(100)
    p.up()
    p.down()

turtle.done()