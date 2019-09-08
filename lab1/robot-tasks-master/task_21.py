#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():

    move_right()
    move_down()

    x = 13

    while x > 1:
        x = x - 1
        for i in range(x):
            fill_cell()
            move_down()
        fill_cell()
        move_right()

        x = x - 1
        for i in range(x):
            fill_cell()
            move_up()
        fill_cell()
        move_right()
        move_down()

    fill_cell()
    move_down()
    move_left(12)

if __name__ == '__main__':
    run_tasks()
