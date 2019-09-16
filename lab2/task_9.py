import turtle as t
import math as m
from time import sleep

t.shape('classic')



def draw(Radius, N):
    center_angle = 360 / N
    angle_of_rotation = center_angle

    t.left(center_angle / 2)

    Center_angle_R = center_angle / 180 * m.pi
    side = 2 * Radius * m.sin(Center_angle_R / 2)

    for j in range(N):
        t.forward(side)
        type(angle_of_rotation)
        t.left(angle_of_rotation)

    t.right(center_angle / 2)



max_polygen = 10
radius = 30
radius_step = 20

t.penup()
t.forward(radius)
t.left(90)
t.pendown()

for i in range(3, max_polygen + 1):
    t.penup()

    t.right(90)
    radius += radius_step
    t.forward(radius_step)
    t.left(90)

    t.pendown()
    draw(radius, i)

pause = 5
sleep(pause)
