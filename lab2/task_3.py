import turtle as t
from time import sleep

t.shape('classic')

side = 100
width = 4
pause = 5

t.penup()
t.goto(-side//2, -side//2)
t.pendown()

t.width(width)

for i in range(4):
    t.forward(side)
    t.left(90)

sleep(pause)
