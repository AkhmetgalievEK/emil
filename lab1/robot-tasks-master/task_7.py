#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():

    while not wall_is_beneath():
        move_down()

    x = 0
    while wall_is_beneath():
        x = x+1
        move_right()

    move_down()
    move_left(x)

if __name__ == '__main__':
    run_tasks()
