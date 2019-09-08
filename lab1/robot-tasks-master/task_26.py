#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():

    for i in range(39):
        if((i+1) % 2 == 1):
            move_down()
            fill_cell()
            for j in range(4):
                move_down(4)
                fill_cell()
            move_up(17)
        elif((i+1) % 4 == 0):
            move_right(2)
        else:
            move_right()
            for a in range(3):
                fill_cell()
                move_down()
            move_up()
            for c in range(4):
                move_down()
                for b in range(3):
                    move_down()
                    fill_cell()
            move_up(18)
            move_right()


    move_down(16)
    move_left(38)


if __name__ == '__main__':
    run_tasks()
