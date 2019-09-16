import turtle as t
from time import sleep

t.shape('classic')

side = 20
side_step = 10
number_of_turns = 10
number_of_iterations = number_of_turns * 4


width = 2
t.width(width)
pause = 5


for i in range(number_of_iterations):
    t.forward(side)
    t.left(90)
    side += side_step


sleep(pause)


