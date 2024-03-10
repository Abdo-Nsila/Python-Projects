import turtle as t
import colorsys as cs

t.setup(800,800)
t.speed(0)
t.width(2)
t.bgcolor("black")
for j in range(100) :
    for i in range(100) :
        t.color(cs.hsv_to_rgb(i/15,j/15,1))
        t.right(90)
        t.circle(90-j*1,100)
        t.left(20)
        t.circle(10-j*1,60)
        t.right(20)
        t.circle(100,150)
t.hideturtle()
t.done()

