import turtle as t
import math
from time import sleep

t.shape('classic')

radius = 100
number_of_sides = 500
angle_of_rotation = 360/number_of_sides
side = angle_of_rotation * math.pi / 180 * radius
width = 0.2
pause = 5
t.speed(10)

t.penup()
t.goto(radius, 0)
t.left(90)
t.pendown()

t.width(width)

for i in range(number_of_sides):
    t.forward(side)
    t.left(angle_of_rotation)

sleep(pause)
