#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():

    flag = True
    while flag or wall_is_beneath():
        if wall_is_beneath():
            flag = False
        move_right()

if __name__ == '__main__':
    run_tasks()
