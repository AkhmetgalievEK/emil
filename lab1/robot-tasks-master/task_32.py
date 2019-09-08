#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():

    if wall_is_above():
        fill_cell()

    count = 0

    while not wall_is_on_the_right():
        move_right()

        if wall_is_above():
            fill_cell()

        if not wall_is_on_the_right():

            x = 0

            while not wall_is_above():
                move_up()
                x = x + 1

                if cell_is_filled():
                    count = count + 1
                else:
                    fill_cell()

            if x:
                move_down(x)

    mov('ax', count)

if __name__ == '__main__':
    run_tasks()
