import turtle as t
import math
from time import sleep

t.shape('classic')

radius = 30
radius_step = 10
number_of_pairs = 9
number_of_sides = 200
angle_of_rotation = 360 / number_of_sides

t.speed(10)
width = 1.2
t.width(width)

def draw_pair(Radius):
    side = angle_of_rotation * math.pi / 180 * Radius

    for i in range(number_of_sides):
        t.forward(side)
        t.left(angle_of_rotation)

    for i in range(number_of_sides):
        t.forward(side)
        t.right(angle_of_rotation)


t.left(90)

for i in range(number_of_pairs + 1):
    draw_pair(radius)
    radius += radius_step

pause = 5
sleep(pause)
