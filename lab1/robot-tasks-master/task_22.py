#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():

    fill_cell()

    while not wall_is_beneath():
        move_down()
        fill_cell()

    while not wall_is_on_the_right():
        move_right()
        fill_cell()

        if wall_is_above():
            while not wall_is_beneath():
                move_down()
                fill_cell()
        else:
            while not wall_is_above():
                move_up()
                fill_cell()

    while not wall_is_on_the_left():
        move_left()

    while not wall_is_beneath():
        move_down()

if __name__ == '__main__':
    run_tasks()
