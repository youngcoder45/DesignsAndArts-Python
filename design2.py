import turtle as t
t=t.Turtle()
s=t.getscreen()
s.bgcolor("white")
t.width(2)
t.speed(15)

col=('black','red','blue')

for i in range(100):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)
s.mainloop()