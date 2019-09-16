import turtle as t
from time import sleep

t.shape('classic')

side = 100
width = 4
pause = 5

t.penup()
t.goto(-side//2, -side)
t.pendown()

t.width(width)

t.forward(side)
t.left(90)
t.forward(side)
t.left(90)
t.forward(side)
t.right(90)
t.forward(side)
t.right(90)
t.forward(side)

sleep(pause)
