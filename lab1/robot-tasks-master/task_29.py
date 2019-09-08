#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    x = 0
    y = 0
    z = 0

    while not wall_is_on_the_right() and x*y*z != 1:
        move_right()
        x = y
        y = z
        z = int(cell_is_filled())


if __name__ == '__main__':
    run_tasks()
