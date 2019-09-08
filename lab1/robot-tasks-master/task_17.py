#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():

    while not cell_is_filled():
        move_up()

    if not wall_is_on_the_left():
        move_left()
        if not cell_is_filled():
            move_right(2)
    else:
        move_right()

if __name__ == '__main__':
    run_tasks()
