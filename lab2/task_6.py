import turtle as t
from time import sleep

t.shape('turtle')


number_of_paws = 12
angle_of_rotation = 360 / number_of_paws


width = 2
t.width(width)
pause = 5


for i in range(number_of_paws):
    t.goto(0, 0)
    t.right(angle_of_rotation)
    t.forward(100)
    t.stamp()
    t.goto(0, 0)

sleep(pause)

