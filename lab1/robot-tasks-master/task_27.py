#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():

    x = 1
    n = 1
    while not wall_is_on_the_right():
        move_right()
        x = x + 1
        if (x == 2 + n*(n - 1)/2):
            n = n + 1
            fill_cell()

if __name__ == '__main__':
    run_tasks()
