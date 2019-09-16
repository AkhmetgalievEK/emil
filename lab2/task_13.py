import turtle as t
import math
from time import sleep

t.shape('classic')

number_of_sides = 200
angle_of_rotation = 360 / number_of_sides
angle_of_rotation_R = angle_of_rotation * math.pi / 180

width_1 = 2
width_2 = 10
t.speed(10)


def draw_a_circle(x, y, R):
    t.penup()
    t.goto(x, y - R)
    t.pendown()
    t.width(width_1)
    t.color('black')

    side = angle_of_rotation_R * R

    for i in range(number_of_sides):
        t.forward(side)
        t.left(angle_of_rotation)


def draw_a_smile(x, y, R):
    t.penup()
    t.goto(x - R, y)
    t.right(90)
    t.pendown()
    t.width(width_2)

    side = angle_of_rotation_R * R

    for i in range(number_of_sides // 2):
        t.forward(side)
        t.left(angle_of_rotation)

    t.right(90)


def draw_a_nose(x, y, L):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.width(width_2)
    t.goto(x, y - L)


x_face = 0
y_face = 0
R_face = 150

t.begin_fill()
draw_a_circle(x_face, y_face, R_face)
t.color('yellow')
t.end_fill()


x_eye = 70
y_eye = 50
R_eye = 30

t.begin_fill()
draw_a_circle(x_eye, y_eye, R_eye)
t.color('blue')
t.end_fill()
t.begin_fill()
draw_a_circle(- x_eye, y_eye, R_eye)
t.color('blue')
t.end_fill()

x_nose = 0
y_nose = 20
L_nose = 60
t.color('black')
draw_a_nose(x_nose, y_nose, L_nose)

x_smile = 0
y_smile = -30
R_smile = 70
t.color('red')
draw_a_smile(x_smile, y_smile, R_smile)


pause = 5
sleep(pause)






