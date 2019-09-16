import turtle as t
import math
from time import sleep

t.shape('classic')

number_of_loops = 5
radius_1 = 50
radius_2 = 20
number_of_sides = 200
angle_of_rotation = 360 / number_of_sides
angle_of_rotation_R = angle_of_rotation * math.pi / 180
side_1 = angle_of_rotation_R * radius_1
side_2 = angle_of_rotation_R * radius_2


def draw_loop():
    for i in range(number_of_sides // 2):
        t.forward(side_1)
        t.right(angle_of_rotation)

    for i in range(number_of_sides // 2):
        t.forward(side_2)
        t.right(angle_of_rotation)


t.penup()
t.goto(-(2 * radius_1 + (number_of_loops - 1) * (2 * radius_1 - 2 * radius_2)) / 2, 0)
t.left(90)
t.pendown()
width = 1
t.width(width)
t.speed(10)


for i in range(number_of_loops):
    draw_loop()


pause = 5
sleep(pause)
