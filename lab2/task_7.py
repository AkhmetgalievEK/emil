import turtle as t
import math
from time import sleep

t.shape('classic')

radius = 80
detail_factor = 100
radius_step = 30/detail_factor
angle_of_rotation = 360/detail_factor
number_of_turns = 3


width = 1
t.width(width)
t.speed(10)
pause = 5


t.penup()
t.goto(radius, 0)
t.left(90)
t.pendown()

for i in range(number_of_turns):
    for j in range(detail_factor):
        shift = angle_of_rotation * math.pi / 180 * radius
        t.forward(shift)
        t.right(90)
        t.forward(radius_step)
        t.left(90 + angle_of_rotation)
        radius += radius_step


sleep(pause)
