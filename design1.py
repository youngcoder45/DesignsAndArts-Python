import turtle as t
import random as r
robot=t.Turtle()
win=t.getscreen()
robot.speed(0)
win.bgcolor("black")
l=["red","green","white","yellow","blue"]
x=10
robot.color("white")
for i in range(100):
    r.shuffle(l)
    robot.pencolor(l[0])
    robot.forward(x)
    robot.left(90)
    x+=10
win.mainloop()
#wow!