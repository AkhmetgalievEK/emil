#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():

    move_down(2)


    fill_cell()

    move_right()
    fill_cell()

    move_up()
    fill_cell()

    move_down(2)
    fill_cell()

    move_right()
    move_up()
    fill_cell()


    for i in range(4):
        move_right(2)
        fill_cell()

        move_right()
        fill_cell()

        move_up()
        fill_cell()

        move_down(2)
        fill_cell()

        move_right()
        move_up()
        fill_cell()


    move_up()
    move_left(2)

if __name__ == '__main__':
    run_tasks()
