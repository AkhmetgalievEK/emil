import turtle as t
import math
from time import sleep

t.shape('classic')

radius = 50
number_of_sides = 100
angle_of_rotation = 360 / number_of_sides
side = angle_of_rotation * math.pi / 180 * radius

t.speed(10)
width = 1
t.width(width)

def draw_pair():
    for i in range(number_of_sides):
        t.forward(side)
        t.left(angle_of_rotation)

    for i in range(number_of_sides):
        t.forward(side)
        t.right(angle_of_rotation)


for i in range(3):
    draw_pair()
    t.left(60)

pause = 5
sleep(pause)

